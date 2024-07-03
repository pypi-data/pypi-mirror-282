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
import os

from django.conf import settings
from django.utils.module_loading import import_string


def str_to_bool(value: str):
    """将字符串转换为 bool 类型，支持 true/false, 0/1"""
    return value.lower() in ("true", "1")


# 变量默认配置
DEFAULT_SETTINGS = {
    # ACCOUNT 相关配置会根据有无配置进行值覆盖，默认不提供，默认值可参考account/sites/default.py
    "ENABLE": {
        "OTEL": {
            # 兼容 paas 内置变量: OTEL_TRACE
            "TRACE": str_to_bool(os.getenv("OTEL_TRACE", "False")),
            "METRIC": False,
        },
        "DD": {
            "PROFILE": False,
        },
    },
    "BKAPP": {
        "OTEL": {
            # 指定服务名称获取方法 类，指定后，将会执行此类的 `get_service_name` 方法来获取 `resource.service_name`
            # （默认获取环境变量/settings 中 BKAPP_OTEL_SERVICE_NAME 的值）
            "SERVICE_NAME_HANDLER": "blueapps.opentelemetry.utils.BlueappsServiceNameHandler",
            # 指定服务版本获取方法类，指定后，将会执行此类的 `get_service_version` 方法来获取 `resource.service_version`
            "SERVICE_VERSION_HANDLER": "blueapps.opentelemetry.utils.ServiceVersionHandler",
            # Trace 上报使用的采样器: OTEL_SAMPLER
            # 兼容 Paas 内置变量
            "SAMPLER": os.getenv("OTEL_SAMPLER", "parentbased_always_on"),
            # grpc 上报地址
            # 兼容 Paas 内置变量: OTEL_GRPC_URL
            "GRPC_HOST": os.getenv("OTEL_GRPC_URL", ""),
            # http 上报地址
            "HTTP_HOST": None,
            # 上报时携带的应用 Token
            # 兼容 Paas 内置变量: OTEL_BK_DATA_TOKEN
            "BK_DATA_TOKEN": os.getenv("OTEL_BK_DATA_TOKEN", ""),
            # 指定 Logging-Instrument 在哪些 LOGGING.formatters 中生效（将会在 formatters 输出中打印 trace 信息）
            "LOGGING_TRACE_FORMATTERS": ("verbose",),
            # Logging 打印时的 Format 格式
            # traceId 占位符为: %(otelTraceID)s，spanId 占位符为 %(otelSpanID)s 服务名称占位符为 %(otelServiceName)s
            "LOGGING_TRACE_FORMAT": "trace_id=%(otelTraceID)s span_id=%(otelSpanID)s",
            # 是否开启对 DB 操作的 Span 记录(如果开启，Span 将会明显增多)
            "INSTRUMENT_DB_API": False,
            # 额外的 Instrumentors
            "ADDTIONAL_INSTRUMENTORS": [],
            # 指定 SpanProcessor
            "SPAN_PROCESSOR_CLS": "blueapps.opentelemetry.trace.export.LazyBatchSpanProcessor",
            # 是否需要在 Django-Instrument 生成的 span 中 将请求参数和 body 记录在 attributes 中，默认开启
            "RECORD_DJANGO_REQUEST_PARAMS": True,
            # 如果需要添加额外的 span_processors，可以配置此值为一个方法的 import 路径
            # 指定后，将会执行此方法获取额外的 span_processors 添加进 traceProvider 中，支持覆盖默认的 span_processors
            "ADDTIONAL_SPAN_PROCESSORS_HANDLER": None,
            # 是否开启 Django-Instrument 的 Hook，如果开启将会记录 request 与 response 相关信息
            "ENABLED_DJANGO_INSTRUMENT_HOOK": True,
            # Django-Instrument 生成的 Span 的 span_name 是否需要替换为 ViewSet 路径 默认开启
            # 此配置当 ENABLED_DJANGO_INSTRUMENT_HOOK 为 True 时生效
            "DJANGO_INSTRUMENT_REPLACE_SPAN_NAME": True,
            # 配置 Django-Instrument / Requests-Instrument Hook 记录请求参数时， 允许的参数最大长度，超过将会截断
            # 此配置当 ENABLED_DJANGO_INSTRUMENT_HOOK 为 True 或者 ENABLED_REQUESTS_INSTRUMENT_HOOK 为 True 时生效
            "RECORD_PARAMS_MAX_SIZE": 10000,
            # 是否开启 Requests-Instrument 的 Hook，如果开启将会记录请求与返回的信息
            "ENABLED_REQUESTS_INSTRUMENT_HOOK": True,
            # 配置 Requests-Instrument 是否需要记录请求参数，默认关闭
            "REQUESTS_INSTRUMENT_RECORD_PARAMS": False,
            # Blueking-Instrument 后置处理
            "INSTRUMENT_HOOK": None,
        },
        "DD_PROFILE": {
            # 上报时携带的应用 Token
            "BK_DATA_TOKEN": "",
            # Profile 需要采样的数据类型 可选: cpu,mem
            "PROFILING_TYPES": ["cpu"],
            # profile 数据上报地址 可以为 bk-collector 或者 pyroscope
            "HOST": "http://localhost:4318",
            # profile 数据上报路径 一般无需更改
            "PATH": "/pyroscope/ingest",
            # 指定额外的 ddtrace patch 处理方法
            "ADDTIONAL_PATCH_CONVERTER": None,
        },
    },
    "IS_AJAX_PLAIN_MODE": False,
    "SPECIFIC_REDIRECT_KEY": None,
    "AJAX_401_RESPONSE_FUNC": None,
    "PAGE_401_RESPONSE_FUNC": None,
    "PAGE_401_RESPONSE_PLATFORM_FUNC": None,
    "NON_REQUEST_USERNAME_PROVIDER": None,
}

# 提供路径需要import_string的变量
IMPORT_SETTINGS = [
    "AJAX_401_RESPONSE_FUNC",
    "PAGE_401_RESPONSE_FUNC",
    "PAGE_401_RESPONSE_PLATFORM_FUNC",
    "BKAPP_OTEL_SPAN_PROCESSOR_CLS",
    "BKAPP_OTEL_SERVICE_NAME_HANDLER",
    "BKAPP_OTEL_SERVICE_VERSION_HANDLER",
    "NON_REQUEST_USERNAME_PROVIDER",
    "BKAPP_OTEL_ADDTIONAL_SPAN_PROCESSORS_HANDLER",
    "BKAPP_OTEL_INSTRUMENT_HOOK",
    "BKAPP_DD_PROFILE_ADDTIONAL_PATCH_CONVERTER",
]

# 在django_settings和blueapps_settings中都支持的配置项
BLUEAPPS_SUPPORT_DJANGO_SETTINGS = [
    "IS_AJAX_PLAIN_MODE",
    "ENABLE_OTEL_TRACE",
    "ENABLE_OTEL_METRIC",
    "ENABLE_DD_PROFILE",
    "BKAPP_OTEL_SERVICE_NAME_HANDLER",
    "BKAPP_OTEL_SERVICE_VERSION_HANDLER",
    "BKAPP_OTEL_SAMPLER",
    "BKAPP_OTEL_HTTP_HOST",
    "BKAPP_OTEL_GRPC_HOST",
    "BKAPP_OTEL_BK_DATA_TOKEN",
    "BKAPP_OTEL_ADDTIONAL_INSTRUMENTORS",
    "BKAPP_OTEL_SPAN_PROCESSOR_CLS",
    "BKAPP_OTEL_INSTRUMENT_DB_API",
    "BKAPP_OTEL_LOGGING_TRACE_FORMATTERS",
    "BKAPP_OTEL_LOGGING_TRACE_FORMAT",
    "BKAPP_OTEL_RECORD_DJANGO_REQUEST_PARAMS",
    "BKAPP_OTEL_ADDTIONAL_SPAN_PROCESSORS_HANDLER",
    "BKAPP_OTEL_ENABLED_DJANGO_INSTRUMENT_HOOK",
    "BKAPP_OTEL_DJANGO_INSTRUMENT_REPLACE_SPAN_NAME",
    "BKAPP_OTEL_RECORD_PARAMS_MAX_SIZE",
    "BKAPP_OTEL_ENABLED_REQUESTS_INSTRUMENT_HOOK",
    "BKAPP_OTEL_REQUESTS_INSTRUMENT_RECORD_PARAMS",
    "BKAPP_OTEL_INSTRUMENT_HOOK",
    "BKAPP_DD_PROFILE_PROFILING_TYPES",
    "BKAPP_DD_PROFILE_HOST",
    "BKAPP_DD_PROFILE_PATH",
    "BKAPP_DD_PROFILE_BK_DATA_TOKEN",
    "BKAPP_DD_PROFILE_ADDTIONAL_PATCH_CONVERTER",
]


class BlueappsSettings:
    SETTING_PREFIX = "BLUEAPPS"
    NESTING_SEPARATOR = "_"

    def __init__(self, default_settings=None, import_strings=None):
        self.project_settings = self.get_flatten_settings(getattr(settings, self.SETTING_PREFIX, {}))
        self.project_settings.update(self.get_django_blueapps_settings())
        self.env_settings = self.get_env_settings(default_settings or DEFAULT_SETTINGS)
        self.default_settings = self.get_flatten_settings(default_settings or DEFAULT_SETTINGS)
        self.import_strings = import_strings or IMPORT_SETTINGS

    def __getattr__(self, key):
        if key not in self.project_settings and key not in self.default_settings:
            raise AttributeError

        # 变量获取优先级: settings > env > default_settings
        try:
            value = self.project_settings[key]
        except KeyError:
            try:
                value = self.env_settings[key]
            except KeyError:
                value = self.default_settings[key]

        if key in self.import_strings and isinstance(value, str):
            try:
                value = import_string(value)
            except ImportError as e:
                message = f"Can not import {value} for Blueapps settings: {e}"
                raise ImportError(message)

        if value is not None:
            setattr(self, key, value)
        return value

    def get_flatten_settings(self, inputted_settings: dict, cur_prefix: str = ""):
        """获取BLUEAPPS配置字典打平之后的配置字典"""

        def get_cur_key(cur_key):
            return f"{cur_prefix}{self.NESTING_SEPARATOR}{cur_key}" if cur_prefix else cur_key

        flatten_settings = {}
        for key, value in inputted_settings.items():
            if isinstance(value, dict):
                flatten_sub_settings = self.get_flatten_settings(value, key)
                flatten_settings.update(
                    {
                        get_cur_key(flatten_key): flatten_value
                        for flatten_key, flatten_value in flatten_sub_settings.items()
                    }
                )
            else:
                flatten_settings[get_cur_key(key)] = value
        return flatten_settings

    def get_django_blueapps_settings(self):
        """获取分散配置在settings中配置项"""
        django_setting_keys = [
            key
            for key in dir(settings)
            if (
                key.startswith(f"{self.SETTING_PREFIX}{self.NESTING_SEPARATOR}")
                or key in BLUEAPPS_SUPPORT_DJANGO_SETTINGS
            )
        ]
        prefix_len = len(f"{self.SETTING_PREFIX}{self.NESTING_SEPARATOR}")
        return {
            key if key in BLUEAPPS_SUPPORT_DJANGO_SETTINGS else key[prefix_len:]: getattr(settings, key)
            for key in django_setting_keys
        }

    def _recursive_env_getter(self, prefix, prefix_value, result):
        """从环境变量中获取具体的值"""
        if isinstance(prefix_value, dict):
            # 如果是嵌套的字典配置，那么继续对嵌套的结果进行查询，知道获取完整的 ENV_KEY
            for key, value in prefix_value.items():
                env_key = f"{prefix}{self.NESTING_SEPARATOR}{key}".upper()
                if isinstance(value, dict):
                    self._recursive_env_getter(env_key, value, result)
                else:
                    env_value = self._get_env_variable(env_key, type(value))
                    if env_value is not None:
                        result[env_key] = env_value
        else:
            # 如果为非嵌套字典，直接获取 ENV_KEY
            env_value = self._get_env_variable(prefix, type(prefix_value))
            if env_value is not None:
                result[prefix] = env_value

    @classmethod
    def _get_env_variable(cls, key, var_type):
        type_func_mapping = {
            str: lambda v: v,
            bool: lambda v: str_to_bool(v),
            int: lambda v: int(v),
            float: lambda v: float(v),
            list: lambda v: v.split(","),
            tuple: lambda v: tuple(v.split(",")),
        }
        value = os.getenv(key)
        if value is None:
            return None
        if var_type is type(None):
            return value

        try:
            return type_func_mapping[var_type](value)
        except (ValueError, TypeError, KeyError):
            return None

    def get_env_settings(self, inputted_settings: dict):
        """获取环境变量中的同名配置"""
        result = {}
        for key, value in inputted_settings.items():
            self._recursive_env_getter(key, value, result)
        return result


blueapps_settings = BlueappsSettings(DEFAULT_SETTINGS, IMPORT_SETTINGS)
