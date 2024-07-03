# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import abc
import json
import logging as _logging
import os
import socket
import sys
from enum import Enum
from typing import Any, Tuple

from django.conf import settings

logger = _logging.getLogger("app")


def inject_logging_trace_info(
    logging: dict,
    inject_formatters: Tuple[str, ...],
    trace_format: str,
    format_keywords: Tuple[str] = ("format", "fmt"),
):
    """往logging配置中动态注入trace信息，直接修改logging数据"""
    formatters = {name: formatter for name, formatter in logging["formatters"].items() if name in inject_formatters}
    for name, formatter in formatters.items():
        matched_keywords = set(format_keywords).intersection(set(formatter.keys()))
        for keyword in matched_keywords:
            formatter.update({keyword: formatter[keyword].strip() + f" {trace_format}\n"})


class BaseServiceNameHandler(abc.ABC):
    @abc.abstractmethod
    def get_service_name(self) -> str:
        ...


class BlueappsServiceNameHandler(BaseServiceNameHandler):
    class SuffixEnum(Enum):
        CELERY_BEAT = "-celery_beat"
        CELERY_WORKER = "-celery_worker"
        NONE = ""

    @property
    def is_celery(self):
        return "celery" in sys.argv

    @property
    def is_celery_beat(self):
        return self.is_celery and "beat" in sys.argv

    @property
    def suffix(self):
        if self.is_celery_beat:
            return self.SuffixEnum.CELERY_BEAT.value
        if self.is_celery:
            return self.SuffixEnum.CELERY_WORKER.value
        return self.SuffixEnum.NONE.value

    def get_service_name(self) -> str:
        app_module_name = getattr(settings, "APP_MODULE_NAME", "")
        service_name = (
            os.getenv("BKAPP_OTEL_SERVICE_NAME")
            or getattr(settings, "BKAPP_OTEL_SERVICE_NAME", None)
            or (settings.APP_CODE + f"-{app_module_name}" if app_module_name else "")
        )
        return f"{service_name}{self.suffix}"


class BaseServiceVersionHandler(abc.ABC):
    @abc.abstractmethod
    def get_service_version(self) -> str:
        ...


class ServiceVersionHandler(BaseServiceVersionHandler):
    def get_service_version(self) -> str:
        # 1. 尝试打开根目录下的 VERSION 文件读取版本号
        version = "0.0.1"
        if os.path.exists(os.path.join(settings.BASE_DIR, "VERSION")):
            try:
                with open(os.path.join(settings.BASE_DIR, "VERSION"), "r", encoding="utf8") as f:
                    version = f.readline().strip()
                    logger.debug(f"[ServiceVersionHandler] retrieve service version: {version}")
            except Exception:  # noqa
                logger.debug(
                    "[ServiceVersionHandler] retrieve version from VERSION file failed, "
                    "service version will not be taken from this file"
                )
        else:
            # 2. 尝试获取配置项中的 version 信息
            if hasattr(settings, "VERSION") and settings.VERSION:
                version = settings.VERSION
                logger.debug(f"[ServiceVersionHandler] retrieve service version: {version}")

        return version


def get_local_ip():
    """
    Returns the actual ip of the local machine.
    This code figures out what source address would be used if some traffic
    were to be sent out to some well known address on the Internet. In this
    case, a Google DNS server is used, but the specific address does not
    matter much.  No traffic is actually sent.
    """
    try:
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(("8.8.8.8", 80))
        (addr, _) = csock.getsockname()
        csock.close()
        return addr
    except socket.error:
        return "127.0.0.1"


def jsonify(data: Any) -> str:
    """尝试将数据转为 JSON 字符串"""
    if not data:
        return ""
    try:
        return json.dumps(data)
    except (TypeError, ValueError):
        if isinstance(data, dict):
            return json.dumps({k: v for k, v in data.items() if not v or isinstance(v, (str, int, float, bool))})
        if isinstance(data, bytes):
            try:
                return data.decode("utf-8")
            except UnicodeDecodeError:
                return str(data)
        return str(data)
