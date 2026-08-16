"""Buda Plugin Info."""

from __future__ import annotations

from typing import Any

from bt_api_base.plugins.protocol import PluginInfo
from bt_api_buda.registry_registration import register_buda


class BudaPluginInfo(PluginInfo):
    """Class BudaPluginInfo"""
    name = "buda"
    version = "0.1.0"
    description = "Buda exchange plugin - Latin American markets (CLP/COP/PEN)"
    supported_modes = {"SPOT"}


def register_plugin(registry: Any, runtime_factory: Any) -> PluginInfo:
    """register_plugin function"""
    register_buda(registry)
    return PluginInfo(
        name="bt_api_buda",
        version="0.1.0",
        core_requires=">=0.15,<1.0",
        supported_exchanges=("BUDA___SPOT",),
        supported_asset_types=("SPOT",),
    )
