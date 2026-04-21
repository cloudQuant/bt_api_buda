from bt_api_base.containers.exchanges.exchange_data import ExchangeData

__all__ = ["BudaExchangeData", "BudaExchangeDataSpot"]


class BudaExchangeData(ExchangeData):
    """Base class for Buda exchange."""

    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "buda"
        self.rest_url = "https://api.buda.com"
        self.wss_url = "wss://api.buda.com/websocket"
        self.kline_periods = {
            "1m": "60",
            "5m": "300",
            "15m": "900",
            "30m": "1800",
            "1h": "3600",
            "4h": "14400",
            "1d": "86400",
            "1w": "604800",
        }
        self.legal_currency = ["CLP", "COP", "PEN", "EUR", "USDT"]


class BudaExchangeDataSpot(BudaExchangeData):
    """Buda Spot exchange configuration."""

    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "spot"
        self.rest_paths = {}
        self.wss_paths = {}
        self.api_key = None
        self.api_secret = None
