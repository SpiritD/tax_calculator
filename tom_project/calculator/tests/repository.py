from decimal import Decimal

from django.test import TestCase
from parameterized import parameterized

from calculator.exceptions import StateNotFound
from calculator.repository import Repository
from calculator.tests.common import fill_db


class RepositoryTestCase(TestCase):
    """Тесты на репозиторий."""

    def setUp(self):
        """Настройка тестов."""
        fill_db()

    @parameterized.expand(
        [
            (Decimal(1), Decimal('0')),
            (Decimal(999), Decimal('0')),
            (Decimal(1000), Decimal('3')),
            (Decimal(1001), Decimal('3')),
            (Decimal(5467), Decimal('5')),
            (Decimal(20000), Decimal('10')),
            (Decimal(200000000), Decimal('15')),
        ],
    )
    def test_get_discount_for_cost(self, cost, expected):
        """Тесты для get_discount_for_cost."""
        repository = Repository()
        self.assertEqual(
            repository.get_discount_for_cost(cost=cost),
            expected,
        )

    @parameterized.expand(
        [
            ('UT', Decimal('6.85')),
            ('NV', Decimal('8')),
            ('TX', Decimal('6.25')),
            ('AL', Decimal('4')),
            ('CA', Decimal('8.25')),
        ],
    )
    def test_get_tax_by_state(self, state_code, expected):
        """Тесты для get_tax_by_state."""
        repository = Repository()
        self.assertEqual(
            repository.get_tax_by_state(state_code=state_code),
            expected,
        )

    def test_bad_state_code(self):
        """Тесты для get_tax_by_state, если нет штата."""
        repository = Repository()
        with self.assertRaises(StateNotFound):
            repository.get_tax_by_state(state_code='QQ')
