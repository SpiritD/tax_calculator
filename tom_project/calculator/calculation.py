from decimal import Decimal

from calculator.repository import Repository


def calculate_total_cost(price: Decimal,
                         quantity: int,
                         state_code: int,
                         repository: Repository) -> Decimal:
    """
    Расчёт итоговой стоимости заказа.

    :param price: цена товара
    :param quantity: количество товара
    :param state_code: код штата
    :param repository: репозиторий для работы с базой
    :return: итоговая стоимость заказа
    """
    cost = price * quantity

    discount = repository.get_discount_for_cost(cost=cost)

    cost *= (100 - discount) / 100

    tax = repository.get_tax_by_state(state_code=state_code)

    return cost * (100 + tax) / 100
