"""Buda plugin registration."""

from __future__ import annotations

from typing import Any

from bt_api_base.balance_utils import simple_balance_handler
from bt_api_base.plugins.protocol import PluginInfo

from bt_api_buda.exchange_data import BudaExchangeDataSpot
from bt_api_buda.feeds.live_buda.spot import BudaRequestDataSpot


BudaPluginInfo = PluginInfo

BUDA_PLUGIN_INFO = PluginInfo(
    name="bt_api_buda",
    version="0.1.1",
    core_requires=">=0.15,<1.0",
    supported_exchanges=("BUDA___SPOT",),
    supported_asset_types=("SPOT",),
)


def register_plugin(registry: Any, runtime_factory: Any | None = None) -> PluginInfo:
    registry.register_feed("BUDA___SPOT", BudaRequestDataSpot)
    registry.register_exchange_data("BUDA___SPOT", BudaExchangeDataSpot)
    registry.register_balance_handler("BUDA___SPOT", simple_balance_handler)
    return BUDA_PLUGIN_INFO
