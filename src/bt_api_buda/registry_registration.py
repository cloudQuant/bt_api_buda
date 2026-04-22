from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler as _buda_balance_handler
from bt_api_base.registry import ExchangeRegistry

from bt_api_buda.exchange_data import BudaExchangeDataSpot
from bt_api_buda.feeds.live_buda.spot import BudaRequestDataSpot


def register_buda() -> None:
    ExchangeRegistry.register_feed("BUDA___SPOT", BudaRequestDataSpot)
    ExchangeRegistry.register_exchange_data("BUDA___SPOT", BudaExchangeDataSpot)
    ExchangeRegistry.register_balance_handler("BUDA___SPOT", _buda_balance_handler)


register_buda()
