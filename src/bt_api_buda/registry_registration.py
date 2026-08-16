"""Module-level docstring."""
from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler as _buda_balance_handler
from bt_api_base.registry import ExchangeRegistry

from bt_api_buda.exchange_data import BudaExchangeDataSpot
from bt_api_buda.feeds.live_buda.spot import BudaRequestDataSpot


def register_buda(registry: ExchangeRegistry | None = None) -> None:
    """register_buda function"""
    target = registry if registry is not None else ExchangeRegistry
    target.register_feed("BUDA___SPOT", BudaRequestDataSpot)
    target.register_exchange_data("BUDA___SPOT", BudaExchangeDataSpot)
    target.register_balance_handler("BUDA___SPOT", _buda_balance_handler)


__all__ = ["register_buda"]
