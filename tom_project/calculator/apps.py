from django.apps import AppConfig


class CalculatorConfig(AppConfig):
    """Конфигурация приложения."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calculator'
