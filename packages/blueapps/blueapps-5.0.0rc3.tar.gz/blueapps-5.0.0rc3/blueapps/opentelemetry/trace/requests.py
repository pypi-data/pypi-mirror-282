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

from opentelemetry.trace import Span, Status, StatusCode
from requests import Response

from blueapps.opentelemetry.utils import jsonify
from blueapps.settings import blueapps_settings


def requests_callback(span: Span, response: Response):
    """
    处理蓝鲸标准协议响应
    """
    if not response:
        return

    try:
        json_result = response.json()
    except Exception:  # pylint: disable=broad-except # noqa
        return

    if not isinstance(json_result, dict):
        return

    # NOTE: esb has a result=bool, but apigateway or other backend maybe has no result
    code = json_result.get("code", 0)
    errors = str(json_result.get("errors", ""))
    if errors:
        span.set_attribute("http.response.errors", errors)

    request_id = (
        # new esb and apigateway
        response.headers.get("x-bkapi-request-id")
        # iam backend
        or response.headers.get("x-request-id")
        # old esb
        or json_result.get("request_id", "")
    )
    if request_id:
        span.set_attribute("request_id", request_id)

    span.set_attribute("http.response.code", code)
    span.set_attribute("http.response.message", json_result.get("message", ""))

    span.set_status(Status(StatusCode.OK if response.ok else StatusCode.ERROR))

    # record request.params
    if blueapps_settings.BKAPP_OTEL_REQUESTS_INSTRUMENT_RECORD_PARAMS:

        req = response.request
        body = req.body

        try:
            authorization_header = req.headers.get("x-bkapi-authorization")
            if authorization_header:
                username = json.loads(authorization_header).get("bk_username")
                if username:
                    span.set_attribute("user.username", username)
        except (TypeError, json.JSONDecodeError):
            if body:
                try:
                    username = json.loads(body).get("bk_username")
                    if username:
                        span.set_attribute("user.username", username)
                except (TypeError, json.JSONDecodeError):
                    pass

        span.set_attribute("request.body", jsonify(body)[: blueapps_settings.BKAPP_OTEL_RECORD_PARAMS_MAX_SIZE])
