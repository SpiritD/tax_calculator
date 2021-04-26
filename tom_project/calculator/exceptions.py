class CalculatorError(Exception):
    """Базовый класс для ошибок в приложении."""


class StateNotFound(CalculatorError):
    """Штат не найден."""
