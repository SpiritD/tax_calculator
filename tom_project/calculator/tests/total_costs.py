from decimal import Decimal

from django.test import TestCase
from parameterized import parameterized

from calculator.calculation import calculate_total_cost
from calculator.exceptions import StateNotFound
from calculator.repository import Repository
from calculator.tests.common import fill_db


class CalculateTotalCostTestCase(TestCase):
    """Тесты на calculate_total_cost."""

    def setUp(self):
        """Настройка тестов."""
        fill_db()

    @parameterized.expand(
        [
            (Decimal(1), 1, 'UT', Decimal('1.0685')),
            (Decimal(1000), 1, 'NV', Decimal('1047.6')),
            (Decimal(1), 1000, 'TX', Decimal('1030.625')),
            (Decimal(200), 100, 'AL', Decimal('18720')),
            (Decimal('123.33'), 175, 'CA', Decimal('21026.9941875')),
        ]
    )
    def test_calculate_total_cost(self, price, quantity, state_code, expected):
        repository = Repository()
        self.assertEqual(
            calculate_total_cost(
                price=price,
                quantity=quantity,
                state_code=state_code,
                repository=repository,
            ),
            expected,
        )

    def test_bad_state_code(self):
        """Проверка неверного кода штата."""
        repository = Repository()
        with self.assertRaises(StateNotFound):
            calculate_total_cost(
                price=Decimal('11.33'),
                quantity=12,
                state_code='WRONG',
                repository=repository,
            )
