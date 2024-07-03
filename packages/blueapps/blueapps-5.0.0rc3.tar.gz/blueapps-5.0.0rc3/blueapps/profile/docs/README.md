# Blueapps Profile 扩展使用说明

Blueapps Profile 为开发者提供了开箱即用的蓝鲸 SaaS Profile 接入工具，你可以通过他来实现上传应用的 Profile 数据，并可以在蓝鲸监控平台中以可视化页面进行查看。

## 使用方法

1️⃣ 安装扩展

```bash
pip install blueapps[profile]
```

2️⃣ 配置 Profile

在 `settings.INSTALLED_APPS` 中加入 `blueapps.profile`

```python
INSTALLED_APPS += (
    ...
    "blueapps.profile",
)
```

在 settings 或者 环境变量中配置为开启并配置上报地址(如果后端接入的是监控平台那么就是 bk-collector 的 http 接口地址)：
```bash
ENABLE_DD_PROFILE=True
BKAPP_DD_PROFILE_HOST=http://127.0.0.1:4318
```

运行后就可以上报数据了，如果接入的是蓝鲸监控平台，接入效果如下：

![Profile](./assets/profile.png)


## 所有配置项

| 名称                                       | 支持环境变量配置 | 支持 django.conf.settings 配置 | 值类型               | 默认值                | 解释                                               |
| ------------------------------------------ | ---------------- | ------------------------------ | -------------------- | --------------------- | -------------------------------------------------- |
| ENABLE_DD_PROFILE                          | ✅                | ✅                              | Bool                 | False                 | 是否开启 Profile 功能                              |
| BKAPP_DD_PROFILE_PROFILING_TYPES           | ✅                | ✅                              | List                 | ["cpu"]               | 需要上报的 profile 数据类型，可选：cpu，mem (内存) |
| BKAPP_DD_PROFILE_HOST                      | ✅                | ✅                              | String               | http://localhost:4318 | profile 数据的后端接收地址                         |
| BKAPP_DD_PROFILE_PATH                      | ✅                | ✅                              | String               | /pyroscope/ingest     | profile 数据的后端接收地址 path                    |
| BKAPP_DD_PROFILE_BK_DATA_TOKEN             | ✅                | ✅                              | String               | <空>                  | profile 数据上报 token                             |
| BKAPP_DD_PROFILE_ADDTIONAL_PATCH_CONVERTER | ✅                | ✅                              | FunctionPath(String) | <空>                  | ddtrace patch 方法                                 |

