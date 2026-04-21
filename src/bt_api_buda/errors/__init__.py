from bt_api_base.error import ErrorTranslator, UnifiedErrorCode

__all__ = ["BudaErrorTranslator"]


class BudaErrorTranslator(ErrorTranslator):
    """Buda exchange error translator."""

    ERROR_MAPPING = {
        "INVALID_CREDENTIALS": UnifiedErrorCode.AUTH_ERROR,
        "CREDENTIALS_MISSING": UnifiedErrorCode.AUTH_ERROR,
        "MARKET_NOT_FOUND": UnifiedErrorCode.SYMBOL_ERROR,
        "INVALID_MARKET": UnifiedErrorCode.SYMBOL_ERROR,
        "INSUFFICIENT_BALANCE": UnifiedErrorCode.BALANCE_ERROR,
        "INVALID_AMOUNT": UnifiedErrorCode.PARAM_ERROR,
        "INVALID_PRICE": UnifiedErrorCode.PARAM_ERROR,
        "ORDER_NOT_FOUND": UnifiedErrorCode.ORDER_NOT_FOUND,
        "RATE_LIMIT": UnifiedErrorCode.RATE_LIMIT_ERROR,
    }

    @staticmethod
    def translate(error_msg: str, status_code: int | None = None) -> UnifiedErrorCode:
        if status_code == 429:
            return UnifiedErrorCode.RATE_LIMIT_ERROR
        for key, code in BudaErrorTranslator.ERROR_MAPPING.items():
            if key in str(error_msg).upper():
                return code
        return UnifiedErrorCode.UNKNOWN_ERROR
