from calculator.models import (
    Discount,
    Tax,
)
from calculator.tests.common import fill_db


# Очищаем базу
Discount.objects.all().delete()
Tax.objects.all().delete()

# Наполняем
fill_db()
