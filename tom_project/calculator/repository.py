from decimal import Decimal
from typing import Optional

from calculator.exceptions import StateNotFound
from calculator.models import (
    Discount,
    Tax,
)


class Repository:
    """Методы для работы с базой."""

    def get_tax_by_state(self, state_code: int) -> Decimal:
        """
        Получение налога для штата в процентах.

        :param state_code: код штата
        :return: величина налога
        """
        try:
            return Tax.objects.get(
                state_code=state_code,
            ).tax
        except Tax.DoesNotExist:
            raise StateNotFound

    def get_discount_for_cost(self, cost: Decimal) -> Decimal:
        """
        Получение величины скидки для стоимости в процентах.

        :param cost: стоисость
        :return: величина скидки
        """
        discount_obj: Optional[Discount] = Discount.objects.filter(
            cost__lte=cost,
        ).order_by(
            '-cost',
        ).first()
        if not discount_obj:
            return Decimal(0)

        return discount_obj.discount
