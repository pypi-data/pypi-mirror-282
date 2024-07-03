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
import json

from django.urls import resolve
from opentelemetry.instrumentation.django import _DjangoMiddleware
from opentelemetry.trace import Status, StatusCode, format_trace_id

from blueapps.core.exceptions import BlueException
from blueapps.opentelemetry.utils import jsonify
from blueapps.settings import blueapps_settings


def django_request_hook(span, request):
    """
    1. 注入trace_id
    2. 记录请求数据
    """
    if not request:
        return

    trace_id = span.get_span_context().trace_id
    request.otel_trace_id = format_trace_id(trace_id)

    if blueapps_settings.BKAPP_OTEL_RECORD_DJANGO_REQUEST_PARAMS:
        try:
            if getattr(request, "FILES", None) and request.method.upper() == "POST":
                # 请求中如果包含了文件 不取 Body 内容
                carrier = request.POST
            else:
                carrier = request.body
        except Exception:  # noqa
            carrier = {}

        body_str = jsonify(carrier) if carrier else ""
        param_str = jsonify(dict(request.GET)) if request.GET else ""

        span.set_attribute(
            "request.body",
            body_str[: blueapps_settings.BKAPP_OTEL_RECORD_PARAMS_MAX_SIZE],
        )
        span.set_attribute(
            "request.params",
            param_str[: blueapps_settings.BKAPP_OTEL_RECORD_PARAMS_MAX_SIZE],
        )


def django_response_hook(span, request, response):
    """
    处理蓝鲸标准协议 Django 响应
    """
    if not request or not response:
        return

    user = getattr(request, "user", None)
    username = getattr(user, "username", "") if user else ""
    span.set_attribute("user.username", username)

    if hasattr(response, "data"):
        result = response.data
    else:
        try:
            result = json.loads(response.content)
        except (TypeError, ValueError, AttributeError):
            return
    if not isinstance(result, dict):
        return

    res_result = result.get("result", True)
    span.set_attribute("http.response.code", result.get("code", 0))
    span.set_attribute("http.response.message", result.get("message", ""))
    span.set_attribute("http.response.result", str(res_result))

    errors = str(result.get("errors", ""))
    if errors:
        span.set_attribute("http.response.errors", errors)
    if res_result:
        span.set_status(Status(StatusCode.OK))
    else:
        span.set_status(Status(StatusCode.ERROR))
        span.record_exception(exception=BlueException(message=result.get("message")))


def get_span_name(_, request):
    try:
        match = resolve(request.path_info)
        return f"{match.func.cls.__module__}.{match.func.cls.__name__}.{match.func.actions[request.method.lower()]}"
    except Exception:  # noqa
        return _DjangoMiddleware.__get_span_name(request)  # pylint: disable=protected-access
