"""Buda Plugin Info."""

from bt_api_base.plugins.protocol import PluginInfo


class BudaPluginInfo(PluginInfo):
    name = "buda"
    version = "0.1.0"
    description = "Buda exchange plugin - Latin American markets (CLP/COP/PEN)"
    supported_modes = {"SPOT"}


def register_plugin():
    pass
