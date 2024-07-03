# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云 - 监控平台 (BlueKing - Monitor) available.
Copyright (C) 2017-2022 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import logging
import os
import socket
from typing import Collection

from celery.signals import beat_init, worker_process_init
from django.conf import settings
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter as GrpcSpanExporter,
)
from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
    OTLPSpanExporter as HttpSpanExporter,
)
from opentelemetry.instrumentation import dbapi
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry.instrumentation.django import DjangoInstrumentor, _DjangoMiddleware
from opentelemetry.instrumentation.instrumentor import BaseInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import SynchronousMultiSpanProcessor, TracerProvider
from opentelemetry.sdk.trace.sampling import _KNOWN_SAMPLERS

from blueapps.opentelemetry.trace.django import (
    django_request_hook,
    django_response_hook,
    get_span_name,
)
from blueapps.opentelemetry.trace.logging import BlueappsLoggingInstrument
from blueapps.opentelemetry.trace.requests import requests_callback
from blueapps.opentelemetry.trace.threading import ThreadingInstrumentor
from blueapps.opentelemetry.utils import get_local_ip
from blueapps.settings import blueapps_settings

logger = logging.getLogger(__name__)


class BlueappsInstrumentor(BaseInstrumentor):
    has_instrument = False
    addtional_instruments = []

    def instrumentation_dependencies(self) -> Collection[str]:
        return []

    @classmethod
    def _get_resource(cls):
        """获取 Resource 对象"""
        resource_info = {
            "service.name": blueapps_settings.BKAPP_OTEL_SERVICE_NAME_HANDLER().get_service_name(),
            "service.version": blueapps_settings.BKAPP_OTEL_SERVICE_VERSION_HANDLER().get_service_version(),
            "service.environment": settings.ENVIRONMENT,
            "bk.data.token": blueapps_settings.BKAPP_OTEL_BK_DATA_TOKEN,
        }

        if os.getenv("BKAPP_OTLP_K8S_BCS_CLUSTER_ID"):
            # 容器环境
            resource_info.update(
                {
                    "k8s.bcs.cluster.id": os.getenv("BKAPP_OTLP_K8S_BCS_CLUSTER_ID"),
                    "k8s.namespace.name": os.getenv("BKAPP_OTLP_K8S_NAMESPACE"),
                    "k8s.pod.ip": get_local_ip(),
                    "k8s.pod.name": socket.gethostname(),
                }
            )
        else:
            # 非容器环境
            resource_info.update(
                {
                    "net.host.ip": get_local_ip(),
                    "net.host.name": socket.gethostname(),
                }
            )

        return Resource.create(resource_info)

    def list_span_processors(self):
        """获取 span 处理器列表"""
        span_processor = blueapps_settings.BKAPP_OTEL_SPAN_PROCESSOR_CLS
        span_processors = []

        if blueapps_settings.BKAPP_OTEL_HTTP_HOST:
            span_processors.append(
                span_processor(HttpSpanExporter(endpoint=blueapps_settings.BKAPP_OTEL_HTTP_HOST))
            )
            if not blueapps_settings.BKAPP_OTEL_BK_DATA_TOKEN:
                logger.warning(
                    "[BlueappsInstrumentor] BK_DATA_TOKEN not set, "
                    f"the http exporter({blueapps_settings.BKAPP_OTEL_HTTP_HOST}) of your application "
                    "will have no data to report",
                )
            else:
                logger.info(f"[BlueappsInstrumentor] trace http exporter: {blueapps_settings.BKAPP_OTEL_HTTP_HOST}")
        elif blueapps_settings.BKAPP_OTEL_GRPC_HOST:
            span_processors.append(
                span_processor(GrpcSpanExporter(endpoint=blueapps_settings.BKAPP_OTEL_GRPC_HOST))
            )
            if not blueapps_settings.BKAPP_OTEL_BK_DATA_TOKEN:
                logger.warning(
                    "[BlueappsInstrumentor] BK_DATA_TOKEN not set, "
                    f"the grpc exporter({blueapps_settings.BKAPP_OTEL_GRPC_HOST}) of your application "
                    "will have no data to report",
                )
            else:
                logger.info(f"[BlueappsInstrumentor] trace grpc exporter: {blueapps_settings.BKAPP_OTEL_GRPC_HOST}")
        else:
            # 按照环境区分
            if settings.ENVIRONMENT == "dev":
                # 本地环境可以使用 jaeger 作为后端
                # 命令：docker run -p 16686:16686 -p 6831:6831/udp jaegertracing/all-in-one
                jaeger_host = os.getenv("BKAPP_OTEL_JAEGER_HOST", "localhost")
                jaeger_exporter = JaegerExporter(
                    agent_host_name=jaeger_host,
                    agent_port=int(os.getenv("BKAPP_OTEL_JAEGER_PORT", 6831)),
                    udp_split_oversized_batches=True,
                )
                span_processors.append(span_processor(jaeger_exporter))
                logger.info(f"[BlueappsInstrumentor] trace jaeger(dev) exporter: {jaeger_host}")
            else:
                logger.warning(
                    "[BlueappsInstrumentor] Currently it is stag environment, "
                    "but neither the <BKAPP_OTEL_GRPC_HOST> or <BKAPP_OTEL_HTTP_HOST> is detected, "
                    "Trace data will not be reported.")

        if blueapps_settings.BKAPP_OTEL_ADDTIONAL_SPAN_PROCESSORS_HANDLER:
            span_processors = blueapps_settings.BKAPP_OTEL_ADDTIONAL_SPAN_PROCESSORS_HANDLER(span_processors)

        return span_processors

    def _instrument(self, **kwargs):

        span_processors = self.list_span_processors()
        sync_span_processor = SynchronousMultiSpanProcessor()
        for i in span_processors:
            sync_span_processor.add_span_processor(i)

        trace_provider = TracerProvider(
            resource=self._get_resource(),
            sampler=_KNOWN_SAMPLERS[blueapps_settings.BKAPP_OTEL_SAMPLER],
            active_span_processor=sync_span_processor,
        )
        trace.set_tracer_provider(trace_provider)

        if blueapps_settings.BKAPP_OTEL_ENABLED_DJANGO_INSTRUMENT_HOOK:
            if blueapps_settings.BKAPP_OTEL_DJANGO_INSTRUMENT_REPLACE_SPAN_NAME:
                setattr(
                    _DjangoMiddleware, "__get_span_name", _DjangoMiddleware._get_span_name
                )  # pylint: disable=protected-access
                _DjangoMiddleware._get_span_name = get_span_name  # pylint: disable=protected-access

            DjangoInstrumentor().instrument(request_hook=django_request_hook, response_hook=django_response_hook)
        else:
            DjangoInstrumentor().instrument()

        if blueapps_settings.BKAPP_OTEL_ENABLED_REQUESTS_INSTRUMENT_HOOK:
            RequestsInstrumentor().instrument(span_callback=requests_callback)
        else:
            RequestsInstrumentor().instrument()

        RedisInstrumentor().instrument()
        BlueappsLoggingInstrument().instrument(
            formatters=blueapps_settings.BKAPP_OTEL_LOGGING_TRACE_FORMATTERS,
            logging_format=blueapps_settings.BKAPP_OTEL_LOGGING_TRACE_FORMAT,
        )
        CeleryInstrumentor().instrument()
        ThreadingInstrumentor().instrument()

        for instrumentor in getattr(blueapps_settings, "BKAPP_OTEL_ADDTIONAL_INSTRUMENTORS", []):
            instrumentor.instrument()
            self.addtional_instruments.append(instrumentor)

        if blueapps_settings.BKAPP_OTEL_INSTRUMENT_DB_API:
            import MySQLdb  # noqa

            dbapi.wrap_connect(
                __name__,
                MySQLdb,
                "connect",
                "mysql",
                {"database": "db", "port": "port", "host": "host", "user": "user"},
            )

        if blueapps_settings.BKAPP_OTEL_INSTRUMENT_HOOK:
            blueapps_settings.BKAPP_OTEL_INSTRUMENT_HOOK()

    def _uninstrument(self, **kwargs):
        DjangoInstrumentor().uninstrument()
        RedisInstrumentor().uninstrument()
        BlueappsLoggingInstrument().uninstrument()
        RequestsInstrumentor().uninstrument()
        CeleryInstrumentor().uninstrument()
        ThreadingInstrumentor().uninstrument()

        for instrument in self.addtional_instruments:
            instrument.uninstrument()


@worker_process_init.connect(weak=False)
def init_celery_worker_tracing(*args, **kwargs):
    if blueapps_settings.ENABLE_OTEL_TRACE:
        BlueappsInstrumentor().instrument()


@beat_init.connect(weak=False)
def init_celery_beat_tracing(*args, **kwargs):
    if blueapps_settings.ENABLE_OTEL_TRACE:
        BlueappsInstrumentor().instrument()
