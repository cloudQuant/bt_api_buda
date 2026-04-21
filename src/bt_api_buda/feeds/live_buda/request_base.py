"""Buda REST API request base class."""

from __future__ import annotations

import hashlib
import hmac
import time
from typing import Any

from bt_api_base.containers.requestdatas.request_data import RequestData
from bt_api_base.feeds.capability import Capability
from bt_api_base.feeds.feed import Feed
from bt_api_base.feeds.http_client import HttpClient
from bt_api_base.logging_factory import get_logger
from bt_api_buda.exchange_data import BudaExchangeDataSpot


class BudaRequestData(Feed):
    @classmethod
    def _capabilities(cls) -> set[Capability]:
        return {
            Capability.GET_TICK,
            Capability.GET_DEPTH,
            Capability.GET_KLINE,
            Capability.GET_EXCHANGE_INFO,
            Capability.GET_BALANCE,
            Capability.GET_ACCOUNT,
            Capability.MAKE_ORDER,
            Capability.CANCEL_ORDER,
        }

    def __init__(self, data_queue: Any = None, **kwargs: Any) -> None:
        super().__init__(data_queue, **kwargs)
        self.data_queue = data_queue
        self.exchange_name = kwargs.get("exchange_name", "BUDA___SPOT")
        self.asset_type = kwargs.get("asset_type", "SPOT")
        self._params = BudaExchangeDataSpot()
        self._params.api_key = kwargs.get("public_key") or kwargs.get("api_key")
        self._params.api_secret = kwargs.get("private_key") or kwargs.get("api_secret")
        self.request_logger = get_logger("buda_feed")
        self.async_logger = get_logger("buda_feed")
        self._http_client = HttpClient(venue=self.exchange_name, timeout=10)

    def _generate_signature(
        self, timestamp: int, method: str, request_path: str, body: str = ""
    ) -> str:
        secret = self._params.api_secret
        if not secret:
            return ""
        sign_str = (
            f"{timestamp}{method}{request_path}{body}"
            if body
            else f"{timestamp}{method}{request_path}"
        )
        return hmac.new(
            secret.encode("utf-8"), sign_str.encode("utf-8"), hashlib.sha256
        ).hexdigest()

    def _get_headers(self, method: str, request_path: str, body: str = "") -> dict:
        timestamp = int(time.time() * 1000)
        headers = {"Content-Type": "application/json"}
        if self._params.api_key:
            headers["X-SBTC-APIKEY"] = self._params.api_key
            headers["X-SBTC-TIMESTAMP"] = str(timestamp)
            headers["X-SBTC-SIGNATURE"] = self._generate_signature(
                timestamp, method, request_path, body
            )
        return headers

    def request(self, path: str, params=None, body=None, extra_data=None, timeout=10):
        method = path.split()[0] if " " in path else "GET"
        request_path = path.split()[1] if " " in path else path
        headers = self._get_headers(method, request_path, str(body) if body else "")
        try:
            response = self._http_client.request(
                method=method,
                url=self._params.rest_url + request_path,
                headers=headers,
                json_data=body if method == "POST" else None,
                params=params,
            )
            return self._process_response(response, extra_data)
        except Exception as e:
            self.request_logger.error(f"Request failed: {e}")
            raise

    async def async_request(self, path: str, params=None, body=None, extra_data=None, timeout=5):
        method = path.split()[0] if " " in path else "GET"
        request_path = path.split()[1] if " " in path else path
        headers = self._get_headers(method, request_path, str(body) if body else "")
        try:
            response = await self._http_client.async_request(
                method=method,
                url=self._params.rest_url + request_path,
                headers=headers,
                json_data=body if method == "POST" else None,
                params=params,
            )
            return self._process_response(response, extra_data)
        except Exception as e:
            self.async_logger.error(f"Async request failed: {e}")
            raise

    def async_callback(self, future):
        try:
            result = future.result()
            if result is not None:
                self.push_data_to_queue(result)
        except Exception as e:
            self.async_logger.error(f"Async callback error: {e}")

    def _process_response(self, response, extra_data=None):
        if extra_data is None:
            extra_data = {}
        return RequestData(response, extra_data)

    def push_data_to_queue(self, data):
        if self.data_queue is not None:
            self.data_queue.put(data)

    def connect(self):
        pass

    def disconnect(self):
        super().disconnect()

    def is_connected(self):
        return True
