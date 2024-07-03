## Quick Start

### 0. 安装扩展

```bash
pip install blueapps[opentelemetry]
```

### 1. 修改 Django 配置

在 `settings.INSTALLED_APPS` 中加入 `blueapps.opentelemetry.trace`

```python
INSTALLED_APPS += (
    ...
    "blueapps.opentelemetry.trace",
)
```

然后打开开关，此配置项支持通过环境变量或者在 django.conf.settings 中配置：

```bash
ENABLE_OTEL_TRACE=True
```

### 2. 配置上报器

上面配置完成后，就打开了 Trace 上报功能，接下来配置将 Trace 上报的哪个地方。

**本地环境**

🚀 如果只想本地观察生成了哪些 span，那么可以使用 ConsoleExporter 来将 Span 打印到控制台上：

```python
def add_console_exporter(span_processor):
    # 增加一个 ConsoleExporter
    span_processor.append(BatchSpanProcessor(ConsoleSpanExporter()))
    return span_processor
```

并在 settings 文件中指定额外的添加 Exporter 方法：
```python
BKAPP_OTEL_ADDTIONAL_SPAN_PROCESSORS_HANDLER = "core.trace.add_console_exporter"
```

这样就会在 blueapps 生成的 Exporter 基础上，新增一个我们自定义的 ConsoleExporter，启动项目后将会看到控制台中有 Span 输出。

🚀 如果不满足只看 Span，还想要以 Trace 视角查看数据，可以选择使用 Jaeger 来作为 Span 的后端接收器。

首先需要安装 Jaeger：

```bash
# 安装 Jaeger
docker run -p 16686:16686 -p 6831:6831/udp jaegertracing/all-in-one
```

安装完成后，启动 Django Server，就可以在 Jaeger 上看到数据了！✌️

![](assets/local_jaeger.png)

**线上预发布/正式环境**

🚀 如果项目需要部署到线上，则需要搭配蓝鲸监控平台使用，上报方式可以选择 Grpc 或者 Http，上报地址为 APM 应用页面中的服务地址。

配置以下环境变量：
```bash
# Http 上报
BKAPP_OTEL_HTTP_HOST = "<监控平台 APM 应用页面上显示的 http 上报地址>"

# 或者 Grpc 上报
BKAPP_OTEL_GRPC_HOST = "<监控平台 APM 应用页面上显示的 grpc 上报地址>"
```

有关于蓝鲸监控平台的提供的 APM 可视化功能，[请参阅这里](https://bk.tencent.com/docs/markdown/ZH/BestPractices/7.1/Monitor/apm_monitor_overview.md)。


## 所有可配置项



| 名称                                                   | 支持环境变量配置 | 支持 django.conf.settings 配置 | 值类型                  | 默认值                                                     | 解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------------------------|----------|----------------------------|----------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BKAPP_OTEL_SERVICE_NAME_HANDLER                      | ✅        | ✅                          | ClassPath)(String)   | blueapps.opentelemetry.utils.BlueappsServiceNameHandler | 指定服务名称获取方法 类，指定后，将会执行此类的 `get_service_name` 方法来获取 `resource.service_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| BKAPP_OTEL_SERVICE_NAME                              | ✅        | ❎                          | String               | <空>                                                     | 指定服务名称（当BKAPP_OTEL_SERVICE_NAME_HANDLER为默认值时生效）                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| BKAPP_OTEL_SERVICE_VERSION_HANDLER                   | ✅        | ✅                          | ClassPath(String)    | blueapps.opentelemetry.utils.ServiceVersionHandler      | 指定服务版本获取方法类，指定后，将会执行此类的 `get_service_version` 方法来获取 `resource.service_version`。默认获取方式为先在项目根目录中寻找 VERSION 文件，找不到再获取 settings.VERSION。                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| BKAPP_OTEL_SAMPLER                                   | ✅        | ✅                          | String               | parentbased_always_on                                   | 配置的是 SDK 上报 trace 时的采样器。<br />一共有六个内置采样器可以选择：<br />1️⃣ always_on： 总是采样，会对所有产生的 span 都进行上报 <br />2️⃣ always_off： 总是不采样，不会上报 span。<br />3️⃣ traceidratio： 根据 traceId 按照比例采样，可以配置一个概率，对 traceId 进行概率采样。<br />4️⃣ parentbased_always_on：始终继承父级采样决策，如果没有父级则始终采样 <br />5️⃣ parentbased_always_off：始终继承父级采样决策，如果没有父级则始终不采样 <br />6️⃣ parentbased_traceidratio：继承父级采样决策，如果没有父级则根据给定的采样率进行采样<br />**配置原则：**<br />SDK 中采样一般可以由最前端的接入层决定，下游中间链路服务可以遵循上游的采样策略，例如上游配置了概率采样后，下游根据上游的采样策略。 如果节点很多，那么开启 always_on 会有大量 span 上报，需要注意量级（如果后端是 bk-collector 则可能会引发限流）。同时在蓝鲸监控平台中也可以配置接收端的采样策略，如概率采样、尾部采样（染色）等策略。 |
| BKAPP_OTEL_GRPC_HOST                                 | ✅        | ✅                          | String               | <空>                                                     | Grpc 方式的上报地址（当 BKAPP_OTEL_GRPC_HOST 和 BKAPP_OTEL_HTTP_HOST 同时存在时，会选择 Http 上报）                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| BKAPP_OTEL_HTTP_HOST                                 | ✅        | ✅                          | String               | <空>                                                     | Http 方式的上报地址（当 BKAPP_OTEL_GRPC_HOST 和 BKAPP_OTEL_HTTP_HOST 同时存在时，会选择 Http 上报）                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| BKAPP_OTEL_BK_DATA_TOKEN                             | ✅        | ✅                          | String               | <空>                                                     | 上报时携带的应用 Token                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| BKAPP_OTEL_LOGGING_TRACE_FORMATTERS                  | ✅        | ✅                          | Tuple                | ("verbose",)                                            | 指定 Logging-Instrument 在哪些 LOGGING.formatters 中生效（将会在 formatters 输出中打印 trace 信息）                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| BKAPP_OTEL_LOGGING_TRACE_FORMAT                      | ✅        | ✅                          | String               | trace_id=%(otelTraceID)s span_id=%(otelSpanID)s         | Logging 打印时的 Format 格式。将会在 BKAPP_OTEL_LOGGING_TRACE_FORMATTERS 配置中指定的 Formatter 输出日志时，将 trace 信息拼接在原始内容的后面。<br />1️⃣ traceId 占位符为: %(otelTraceID)s<br />2️⃣ spanId 占位符为 %(otelSpanID)s <br />3️⃣ 服务名称占位符为 %(otelServiceName)s                                                                                                                                                                                                                                                                                                                                                                |
| BKAPP_OTEL_INSTRUMENT_DB_API                         | ✅        | ✅                          | Bool                 | False                                                   | 是否开启对 DB 操作的 Span 记录(如果开启，Span 将会明显增多)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| BKAPP_OTEL_ADDTIONAL_INSTRUMENTORS                   | ✅        | ✅                          | List                 | <空>                                                     | 额外的 Instrumentors。（列表的值需要为 Instrument 的 import 路径）                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| BKAPP_OTEL_SPAN_PROCESSOR_CLS                        | ✅        | ✅                          | ClassPath(String)    | blueapps.opentelemetry.export.LazyBatchSpanProcessor    | 指定使用的 SpanProcessor 类                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| BKAPP_OTEL_RECORD_DJANGO_REQUEST_PARAMS              | ✅        | ✅                          | Bool                 | True                                                    | 是否需要在 Django-Instrument 生成的 span 中 将请求参数和 body 记录在 attributes 中，默认开启                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| BKAPP_OTEL_ADDTIONAL_SPAN_PROCESSORS_HANDLER         | ✅        | ✅                          | FunctionPath(String) | <空>                                                     | 如果需要添加额外的 span_processors，可以配置此值为一个方法的 import 路径，指定后，将会执行此方法获取额外的 span_processors 添加进 traceProvider 中，支持覆盖默认的 span_processors。                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| BKAPP_OTEL_ENABLED_DJANGO_INSTRUMENT_HOOK            | ✅        | ✅                          | Bool                 | True                                                    | 是否开启 Django-Instrument 的 Hook，如果开启将会记录 request 与 response 相关信息                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| BKAPP_OTEL_DJANGO_INSTRUMENT_REPLACE_SPAN_NAME       | ✅        | ✅                          | Bool                 | True                                                    | Django-Instrument 生成的 Span 的 span_name 是否需要替换为 ViewSet 路径 默认开启。（此配置当 BKAPP_OTEL_ENABLED_DJANGO_INSTRUMENT_HOOK 为 True 时生效）<br />开启前后 span_name 对比：<br />`'healthz/$'` 👉 `'apps.entry.views.EntryViewSet.healthz'`                                                                                                                                                                                                                                                                                                                                                                           |
| BKAPP_OTEL_RECORD_PARAMS_MAX_SIZE | ✅        | ✅                          | Integer              | 10000                                                   | 配置 Django-Instrument / Requests-Instrument Hook 记录请求参数时， 允许的参数最大长度，超过将会截断（此配置当 ENABLED_DJANGO_INSTRUMENT_HOOK 为 True 或者 ENABLED_REQUESTS_INSTRUMENT_HOOK 为 True 时生效）                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| BKAPP_OTEL_ENABLED_REQUESTS_INSTRUMENT_HOOK          | ✅        | ✅                          | Bool                 | True                                                    | 是否开启 Requests-Instrument 的 Hook，如果开启将会记录请求与返回的信息                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| BKAPP_OTEL_REQUESTS_INSTRUMENT_RECORD_PARAMS         | ✅        | ✅                          | Bool                 | False                                                   | 配置 Requests-Instrument 是否需要记录请求参数，默认关闭                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| BKAPP_OTEL_INSTRUMENT_HOOK                           | ✅        | ✅                          | FunctionPath(String) | <空>                                                     | Blueking-Instrument 后置处理                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 【🌟容器环境推荐配置】BKAPP_OTLP_K8S_BCS_CLUSTER_ID            | ✅        | ❎                          | String               | <空>                                                     | 如果项目部署在容器环境，推荐配置此环境变量，指定项目部署所在的 K8S 集群 ID，配置后，此值将会记录在 `resource.k8s.bcs.cluster.id` 字段中。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 【🌟容器环境推荐配置】BKAPP_OTLP_K8S_NAMESPACE                 | ✅        | ❎                          | String               | <空>                                                     | 如果项目部署在容器环境，推荐配置此环境变量，指定项目部署所在的 K8S 命名空间名称，配置后，此值将会记录在 `resource.k8s.namespace.name` 字段中。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| BKAPP_OTEL_JAEGER_HOST                               | ✅        | ❎                          | String               | localhost                                               | 指定本地上报Span 到 Jaeger时的 Jaeger 接收地址。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| BKAPP_OTEL_JAEGER_PORT                               | ✅        | ❎                          | Integer              | 6831                                                    | 指定本地上报Span 到 Jaeger时的 Jaeger 接收端口。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |



如果配置项支持 `django.conf.settings` 与 环境变量 同时配置，那么**优先级是：django.conf.settings > 环境变量 > 默认值**

> 这里所说的 django.conf.settings 配置，意思是遵循 blueapps 的配置方式，例如：
> ```python
> BLUEAPPS = {
>    "BKAPP": {
>        "OTEL": {
>            "ADDTIONAL_SPAN_PROCESSORS_HANDLER": "core.trace.add_console_exporter"
>        }
>    }
> }
> ```
> 或者：
> ```python
> BKAPP_OTEL_ADDTIONAL_SPAN_PROCESSORS_HANDLER = "core.trace.add_console_exporter"
> ```

### 🌅 旧版本升级指引

如果你的项目中 blueapps 版本为 < 5.0.0，现在想升级到 5.x 版本，需要修改 trace 中有关的配置项。

settings 调整：

1️⃣ `INSTALL_APPS` 更变:

旧:
```python
INSTALLED_APPS += (
    ...
    "blueapps.opentelemetry.instrument_app",
)
```

新:
```python
INSTALLED_APPS += (
    ...
    "blueapps.opentelemetry.trace",
)
```

2️⃣ 配置项调整:

如果你使用了以下配置项配置过 trace，那么需要更变为新的形式。（如下无特别说明则代表未更变）

1. [更名] `BK_APP_OTEL_INSTRUMENT_DB_API` -> `BKAPP_OTEL_INSTRUMENT_DB_API`

2. [更名] `BK_APP_OTEL_ADDTIONAL_INSTRUMENTORS` -> `BKAPP_OTEL_ADDTIONAL_INSTRUMENTORS`

3. [更名 + 类型更变] `BLUEAPPS_BKAPP_OTEL_SPAN_PROCESSOR` -> `BKAPP_OTEL_SPAN_PROCESSOR_CLS` 
   1. 类型变更: 原先值类型为 class，现在值类型为 class 的 import_path 字符串格式。

4. [默认值变更] `BKAPP_OTEL_SAMPLER` 的默认值由 `parentbased_always_off` 改为 `parentbased_always_on`

5. [默认行为变更] 旧版本中默认使用 `grpc` 方式上报（涉及变量：`BKAPP_OTEL_GRPC_HOST`），新版本中默认使用 `http` 上报。（涉及变量：`BKAPP_OTEL_EXPORTER_TYPE`、`BKAPP_OTEL_HTTP_HOST`、`BKAPP_OTEL_GRPC_HOST`）

6. [更名 + 默认值更变] `OTEL_LOGGING_TRACE_FORMAT` -> `BKAPP_OTEL_LOGGING_TRACE_FORMAT`
   1. 此变量的默认值由 `"[trace_id]: %(otelTraceID)s [span_id]: %(otelSpanID)s [resource.service.name]: %(otelServiceName)s"` 改为 `trace_id=%(otelTraceID)s span_id=%(otelSpanID)s`

7. [删除] 删除 `BKAPP_OTEL_BK_DATA_ID`，统一使用 `BKAPP_OTEL_BK_DATA_TOKEN`
