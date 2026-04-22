# bt_api_buda

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_buda.svg)](https://pypi.org/project/bt_api_buda/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_buda.svg)](https://pypi.org/project/bt_api_buda/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_buda/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_buda/actions)
[![Docs](https://readthedocs.org/projects/bt-api-buda/badge/?version=latest)](https://bt-api-buda.readthedocs.io/)

---

<!-- English -->
# bt_api_buda

> **Buda exchange plugin for bt_api** — Unified REST API for **Spot** trading with support for Latin American markets.

`bt_api_buda` is a runtime plugin for [bt_api](https://github.com/cloudQuant/bt_api_py) that connects to **Buda** exchange. It depends on [bt_api_base](https://github.com/cloudQuant/bt_api_base) for core infrastructure.

| Resource | Link |
|----------|------|
| English Docs | https://bt-api-buda.readthedocs.io/ |
| Chinese Docs | https://bt-api-buda.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_buda |
| PyPI | https://pypi.org/project/bt_api_buda/ |
| Issues | https://github.com/cloudQuant/bt_api_buda/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://github.com/cloudQuant/bt_api_py |

---

## Features

### Spot Trading

| Feature | Status | Description |
|---|---|---|
| Ticker | ✅ | Market ticker with 24hr stats |
| Order Book | ✅ | Depth data with bid/ask prices |
| K-Lines | ✅ | Candlestick charts (1m to 1w) |
| Trade History | ✅ | Recent trades |
| Exchange Info | ✅ | Market listings and trading rules |
| Account Balance | ✅ | User balance across all assets |
| Place Order | ✅ | Limit orders (Bid/Ask) |
| Cancel Order | ✅ | Cancel pending orders |
| Query Order | ✅ | Get order status by ID |
| Open Orders | ✅ | List all pending orders |

### Supported Markets

Buda supports trading in **4 fiat currencies** and **USDT**:

| Currency | Code | Type |
|---|---|---|
| Chilean Peso | `CLP` | Fiat |
| Colombian Peso | `COP` | Fiat |
| Peruvian Sol | `PEN` | Fiat |
| Euro | `EUR` | Fiat |
| Tether | `USDT` | Stablecoin |

### Supported Trading Pairs

Buda markets include popular pairs such as:

- `BTC-CLP`, `ETH-CLP`, `USDT-CLP`
- `BTC-COP`, `ETH-COP`, `USDT-COP`
- `BTC-PEN`, `ETH-PEN`, `USDT-PEN`
- `BTC-EUR`, `ETH-EUR`, `USDT-EUR`
- `BTC-USDT`, `ETH-USDT`

### Plugin Architecture

Auto-registers at import time via `ExchangeRegistry`. Works seamlessly with `BtApi`:

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BUDA___SPOT": {
        "api_key": "your_public_key",
        "secret": "your_private_key",
    }
})

# Get ticker (public - no auth required)
ticker = api.get_tick("BUDA___SPOT", "BTC-CLP")

# Get balance (requires auth)
balance = api.get_balance("BUDA___SPOT")

# Place order (requires auth)
order = api.make_order(
    exchange_name="BUDA___SPOT",
    symbol="BTC-CLP",
    volume=0.001,
    price=50000000,
    order_type="limit",
)
```

---

## Installation

### From PyPI (Recommended)

```bash
pip install bt_api_buda
```

### From Source

```bash
git clone https://github.com/cloudQuant/bt_api_buda
cd bt_api_buda
pip install -e .
```

### Requirements

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

---

## Quick Start

### 1. Install

```bash
pip install bt_api_buda
```

### 2. Get ticker (public — no API key needed)

```python
from bt_api_py import BtApi

api = BtApi()
ticker = api.get_tick("BUDA___SPOT", "BTC-CLP")
print(f"BTC-CLP price: {ticker}")
```

### 3. Place an order (requires API key)

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BUDA___SPOT": {
        "api_key": "your_public_key",
        "secret": "your_private_key",
    }
})

order = api.make_order(
    exchange_name="BUDA___SPOT",
    symbol="BTC-CLP",
    volume=0.001,
    price=50000000,
    order_type="limit",
)
print(f"Order placed: {order}")
```

---

## Architecture

```
bt_api_buda/
├── plugin.py                     # register_plugin() — bt_api plugin entry point
├── registry_registration.py      # register_buda() — feeds / exchange_data / balance_handler registration
├── exchange_data/
│   └── __init__.py             # BudaExchangeData, BudaExchangeDataSpot
├── feeds/
│   └── live_buda/
│       ├── spot.py            # BudaRequestDataSpot — all spot operations
│       └── request_base.py   # BudaRequestData — REST base class
└── errors/
    └── __init__.py            # Error definitions
```

---

## Supported Operations

| Category | Operation | Notes |
|---|---|---|
| **Market Data** | `get_tick` | 24hr rolling ticker |
| | `get_depth` | Order book depth |
| | `get_kline` | Candlestick/k-line data |
| | `get_exchange_info` | Market listings |
| **Account** | `get_balance` | All asset balances |
| | `get_account` | Full account info |
| | `get_open_orders` | All pending orders |
| | `query_order` | Single order by ID |
| **Trading** | `make_order` | Limit orders (Bid/Ask) |
| | `cancel_order` | Cancel pending order |

---

## Rate Limits

| Endpoint | Limit |
|---|---|
| General | 60 requests/minute |
| Trading | 30 requests/minute |

---

## Error Handling

All Buda API errors are translated to bt_api_base error types:

| Error | Description |
|---|---|
| `API_ERROR` | Unknown error |
| `RATE_LIMIT` | Rate limit exceeded |
| `INVALID_PARAMETER` | Invalid parameter |
| `SIGNATURE_INVALID` | Invalid signature |
| `API_KEY_MISSING` | API key not provided |
| `ORDER_NOT_FOUND` | Order does not exist |
| `BALANCE_INSUFFICIENT` | Insufficient balance |

---

## Documentation

| Doc | Link |
|-----|------|
| **English** | https://bt-api-buda.readthedocs.io/ |
| **中文** | https://bt-api-buda.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://cloudquant.github.io/bt_api_py/ |

---

## License

MIT — see [LICENSE](LICENSE).

---

## Support

- [GitHub Issues](https://github.com/cloudQuant/bt_api_buda/issues) — bug reports, feature requests
- Email: yunjinqi@gmail.com

---

---

## 中文

> **bt_api 的 Buda 交易所插件** — 为**现货**交易提供统一的 REST API，支持拉丁美洲市场。

`bt_api_buda` 是 [bt_api](https://github.com/cloudQuant/bt_api_py) 的运行时插件，连接 **Buda** 交易所。依赖 [bt_api_base](https://github.com/cloudQuant/bt_api_base) 提供核心基础设施。

| 资源 | 链接 |
|------|------|
| 英文文档 | https://bt-api-buda.readthedocs.io/ |
| 中文文档 | https://bt-api-buda.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_buda |
| PyPI | https://pypi.org/project/bt_api_buda/ |
| 问题反馈 | https://github.com/cloudQuant/bt_api_buda/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://github.com/cloudQuant/bt_api_py |

---

## 功能特点

### 现货交易

| 功能 | 状态 | 说明 |
|---|---|---|
| 行情 | ✅ | 24小时滚动行情 |
| 订单簿 | ✅ | 深度数据（买/卖价） |
| K线 | ✅ | 蜡烛图（1分钟到1周） |
| 成交历史 | ✅ | 近期成交 |
| 交易所信息 | ✅ | 市场列表和交易规则 |
| 账户余额 | ✅ | 全资产余额查询 |
| 下单 | ✅ | 限价单（买入/卖出） |
| 撤单 | ✅ | 取消挂单 |
| 订单查询 | ✅ | 按ID查询订单状态 |
| 挂单列表 | ✅ | 所有待成交订单 |

### 支持的市场

Buda 支持 **4 种法币** 和 **USDT** 交易：

| 货币 | 代码 | 类型 |
|---|---|---|
| 智利比索 | `CLP` | 法币 |
| 哥伦比亚比索 | `COP` | 法币 |
| 秘鲁索尔 | `PEN` | 法币 |
| 欧元 | `EUR` | 法币 |
| 泰达币 | `USDT` | 稳定币 |

### 支持的交易对

Buda 市场包括：

- `BTC-CLP`, `ETH-CLP`, `USDT-CLP`
- `BTC-COP`, `ETH-COP`, `USDT-COP`
- `BTC-PEN`, `ETH-PEN`, `USDT-PEN`
- `BTC-EUR`, `ETH-EUR`, `USDT-EUR`
- `BTC-USDT`, `ETH-USDT`

### 插件架构

通过 `ExchangeRegistry` 在导入时自动注册，与 `BtApi` 无缝协作：

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BUDA___SPOT": {
        "api_key": "your_public_key",
        "secret": "your_private_key",
    }
})

# 获取行情（公开接口，无需认证）
ticker = api.get_tick("BUDA___SPOT", "BTC-CLP")

# 获取余额（需要认证）
balance = api.get_balance("BUDA___SPOT")

# 下单（需要认证）
order = api.make_order(
    exchange_name="BUDA___SPOT",
    symbol="BTC-CLP",
    volume=0.001,
    price=50000000,
    order_type="limit",
)
```

---

## 安装

### 从 PyPI 安装（推荐）

```bash
pip install bt_api_buda
```

### 从源码安装

```bash
git clone https://github.com/cloudQuant/bt_api_buda
cd bt_api_buda
pip install -e .
```

### 系统要求

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

---

## 快速开始

### 1. 安装

```bash
pip install bt_api_buda
```

### 2. 获取行情（公开接口，无需 API key）

```python
from bt_api_py import BtApi

api = BtApi()
ticker = api.get_tick("BUDA___SPOT", "BTC-CLP")
print(f"BTC-CLP 价格: {ticker}")
```

### 3. 下单交易（需要 API key）

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BUDA___SPOT": {
        "api_key": "your_public_key",
        "secret": "your_private_key",
    }
})

order = api.make_order(
    exchange_name="BUDA___SPOT",
    symbol="BTC-CLP",
    volume=0.001,
    price=50000000,
    order_type="limit",
)
print(f"订单已下单: {order}")
```

---

## 架构

```
bt_api_buda/
├── plugin.py                     # register_plugin() — bt_api 插件入口点
├── registry_registration.py     # register_buda() — feeds / exchange_data / balance_handler 注册
├── exchange_data/
│   └── __init__.py             # BudaExchangeData, BudaExchangeDataSpot
├── feeds/
│   └── live_buda/
│       ├── spot.py            # BudaRequestDataSpot — 所有现货操作
│       └── request_base.py   # BudaRequestData — REST 基类
└── errors/
    └── __init__.py            # 错误定义
```

---

## 支持的操作

| 类别 | 操作 | 说明 |
|---|---|---|
| **行情数据** | `get_tick` | 24小时滚动行情 |
| | `get_depth` | 订单簿深度 |
| | `get_kline` | K线/蜡烛图数据 |
| | `get_exchange_info` | 市场列表 |
| **账户** | `get_balance` | 所有资产余额 |
| | `get_account` | 完整账户信息 |
| | `get_open_orders` | 所有挂单 |
| | `query_order` | 按ID查询订单 |
| **交易** | `make_order` | 限价单（买入/卖出） |
| | `cancel_order` | 取消挂单 |

---

## 限流配置

| 端点 | 限制 |
|---|---|
| 通用 | 60 次/分钟 |
| 交易 | 30 次/分钟 |

---

## 错误处理

所有 Buda API 错误均翻译为 bt_api_base 错误类型：

| 错误 | 说明 |
|---|---|
| `API_ERROR` | 未知错误 |
| `RATE_LIMIT` | 请求过于频繁 |
| `INVALID_PARAMETER` | 无效参数 |
| `SIGNATURE_INVALID` | 无效签名 |
| `API_KEY_MISSING` | 未提供 API key |
| `ORDER_NOT_FOUND` | 订单不存在 |
| `BALANCE_INSUFFICIENT` | 余额不足 |

---

## 文档

| 文档 | 链接 |
|-----|------|
| **英文文档** | https://bt-api-buda.readthedocs.io/ |
| **中文文档** | https://bt-api-buda.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://cloudquant.github.io/bt_api_py/ |

---

## 许可证

MIT — 详见 [LICENSE](LICENSE)。

---

## 技术支持

- [GitHub Issues](https://github.com/cloudQuant/bt_api_buda/issues) — bug 报告、功能请求
- 邮箱: yunjinqi@gmail.com
