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
from typing import Collection, Tuple

from django.conf import settings
from django.utils.log import configure_logging
from opentelemetry.instrumentation.instrumentor import BaseInstrumentor
from opentelemetry.trace import (
    INVALID_SPAN,
    INVALID_SPAN_CONTEXT,
    get_current_span,
    get_tracer_provider,
)

from blueapps.opentelemetry.utils import inject_logging_trace_info


class BlueappsLoggingInstrument(BaseInstrumentor):
    __doc__ = """Logging-Instrument for Blueapps"""

    _old_factory = None

    def instrumentation_dependencies(self) -> Collection[str]:
        return tuple()

    def _instrument(self, formatters: Tuple[str, ...] = None, logging_format: str = None, **kwargs):
        provider = kwargs.get("tracer_provider", None) or get_tracer_provider()
        old_factory = logging.getLogRecordFactory()
        BlueappsLoggingInstrument._old_factory = old_factory

        service_name = None

        def record_factory(*args, **kwargs):
            record = old_factory(*args, **kwargs)

            record.otelSpanID = "0"
            record.otelTraceID = "0"

            nonlocal service_name
            if service_name is None:
                resource = getattr(provider, "resource", None)
                if resource:
                    service_name = resource.attributes.get("service.name") or ""
                else:
                    service_name = ""

            record.otelServiceName = service_name

            span = get_current_span()
            if span != INVALID_SPAN:
                ctx = span.get_span_context()
                if ctx != INVALID_SPAN_CONTEXT:
                    record.otelSpanID = format(ctx.span_id, "016x")
                    record.otelTraceID = format(ctx.trace_id, "032x")
            return record

        logging.setLogRecordFactory(record_factory)

        # default behavior is to concatenate after the origin content
        inject_logging_trace_info(settings.LOGGING, formatters, logging_format)
        configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)

    def _uninstrument(self, **kwargs):
        if BlueappsLoggingInstrument._old_factory:
            logging.setLogRecordFactory(BlueappsLoggingInstrument._old_factory)
            BlueappsLoggingInstrument._old_factory = None
