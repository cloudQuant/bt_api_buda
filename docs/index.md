# BUDA Documentation

<!-- English -->
## English

Welcome to the **BUDA** documentation for bt_api.

**BUDA** (formerly Streamflow) is a Latin American cryptocurrency exchange headquartered in Santiago, Chile. It supports trading in CLP (Chilean Peso), COP (Colombian Peso), PEN (Peruvian Sol), EUR (Euro), and USDT.

### Overview

`bt_api_buda` provides a unified interface to Buda exchange through the bt_api plugin architecture. It supports:

- **Market Data**: Ticker, Order Book, K-Lines, Trade History
- **Account**: Balance, Open Orders, Order Status
- **Trading**: Place Limit Orders, Cancel Orders

### Installation

```bash
pip install bt_api_buda
```

### Quick Start

```python
from bt_api_py import BtApi

# Initialize without authentication (public data only)
api = BtApi()

# Get ticker (public)
ticker = api.get_tick("BUDA___SPOT", "BTC-CLP")
print(f"BTC-CLP: {ticker}")

# With authentication
api_auth = BtApi(exchange_kwargs={
    "BUDA___SPOT": {
        "api_key": "your_public_key",
        "secret": "your_private_key",
    }
})

# Get balance
balance = api_auth.get_balance("BUDA___SPOT")

# Place order
order = api_auth.make_order(
    exchange_name="BUDA___SPOT",
    symbol="BTC-CLP",
    volume=0.001,
    price=50000000,
    order_type="limit",
)
```

### Supported Operations

| Operation | Auth Required | Description |
|-----------|---------------|-------------|
| `get_tick` | No | 24hr rolling ticker |
| `get_depth` | No | Order book depth |
| `get_kline` | No | Candlestick data |
| `get_exchange_info` | No | Market listings |
| `get_balance` | Yes | Asset balances |
| `get_account` | Yes | Account information |
| `get_open_orders` | Yes | Pending orders |
| `query_order` | Yes | Order by ID |
| `make_order` | Yes | Place limit order |
| `cancel_order` | Yes | Cancel order |

### Supported Markets

| Currency | Code | Type |
|----------|------|------|
| Chilean Peso | CLP | Fiat |
| Colombian Peso | COP | Fiat |
| Peruvian Sol | PEN | Fiat |
| Euro | EUR | Fiat |
| Tether | USDT | Stablecoin |

### Exchange Code

```
BUDA___SPOT
```

### Error Handling

All API errors are translated to bt_api_base standard errors:

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BUDA___SPOT": {
        "api_key": "invalid_key",
        "secret": "invalid_secret",
    }
})

try:
    balance = api.get_balance("BUDA___SPOT")
except Exception as e:
    print(f"Error: {e}")
```

### Rate Limits

- **Public endpoints**: 60 requests/minute
- **Trading endpoints**: 30 requests/minute

### More Information

- [GitHub Repository](https://github.com/cloudQuant/bt_api_buda)
- [Issue Tracker](https://github.com/cloudQuant/bt_api_buda/issues)
- [bt_api Documentation](https://cloudquant.github.io/bt_api_py/)
- [bt_api_base Documentation](https://bt-api-base.readthedocs.io/)

---

## 中文

欢迎使用 bt_api 的 **BUDA** 文档。

**BUDA**（前身为 Streamflow）是一家总部位于智利圣地亚哥的拉丁美洲加密货币交易所。支持 CLP（智利比索）、COP（哥伦比亚比索）、PEN（秘鲁索尔）、EUR（欧元）和 USDT 交易。

### 概述

`bt_api_buda` 通过 bt_api 插件架构提供连接 Buda 交易所的统一接口。支持：

- **行情数据**：行情、订单簿、K线、成交历史
- **账户**：余额、挂单列表、订单状态
- **交易**：下限价单、撤单

### 安装

```bash
pip install bt_api_buda
```

### 快速开始

```python
from bt_api_py import BtApi

# 初始化（无需认证，仅获取公开数据）
api = BtApi()

# 获取行情（公开接口）
ticker = api.get_tick("BUDA___SPOT", "BTC-CLP")
print(f"BTC-CLP: {ticker}")

# 需要认证的操作
api_auth = BtApi(exchange_kwargs={
    "BUDA___SPOT": {
        "api_key": "your_public_key",
        "secret": "your_private_key",
    }
})

# 获取余额
balance = api_auth.get_balance("BUDA___SPOT")

# 下单
order = api_auth.make_order(
    exchange_name="BUDA___SPOT",
    symbol="BTC-CLP",
    volume=0.001,
    price=50000000,
    order_type="limit",
)
```

### 支持的操作

| 操作 | 需要认证 | 说明 |
|------|---------|------|
| `get_tick` | 否 | 24小时滚动行情 |
| `get_depth` | 否 | 订单簿深度 |
| `get_kline` | 否 | K线数据 |
| `get_exchange_info` | 否 | 市场列表 |
| `get_balance` | 是 | 资产余额 |
| `get_account` | 是 | 账户信息 |
| `get_open_orders` | 是 | 挂单列表 |
| `query_order` | 是 | 按ID查询订单 |
| `make_order` | 是 | 下限价单 |
| `cancel_order` | 是 | 撤单 |

### 支持的市场

| 货币 | 代码 | 类型 |
|------|------|------|
| 智利比索 | CLP | 法币 |
| 哥伦比亚比索 | COP | 法币 |
| 秘鲁索尔 | PEN | 法币 |
| 欧元 | EUR | 法币 |
| 泰达币 | USDT | 稳定币 |

### 交易所代码

```
BUDA___SPOT
```

### 错误处理

所有 API 错误都会翻译为 bt_api_base 标准错误：

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BUDA___SPOT": {
        "api_key": "invalid_key",
        "secret": "invalid_secret",
    }
})

try:
    balance = api.get_balance("BUDA___SPOT")
except Exception as e:
    print(f"错误: {e}")
```

### 限流配置

- **公开接口**：60 次/分钟
- **交易接口**：30 次/分钟

### 更多信息

- [GitHub 仓库](https://github.com/cloudQuant/bt_api_buda)
- [问题反馈](https://github.com/cloudQuant/bt_api_buda/issues)
- [bt_api 文档](https://cloudquant.github.io/bt_api_py/)
- [bt_api_base 文档](https://bt-api-base.readthedocs.io/)
