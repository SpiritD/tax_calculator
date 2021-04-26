# import os, django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tom_project.settings')
# django.setup()

from decimal import Decimal

from calculator.models import Discount, Tax


discounts = {
    1_000: 3,
    5_000: 5,
    7_000: 7,
    10_000: 10,
    50_000: 15,
}


Discount.objects.all().delete()

discount_objects = []
for cost, discount in discounts.items():
    discount_objects.append(
        Discount(
            cost=cost,
            discount=discount,
        ),
    )

Discount.objects.bulk_create(discount_objects)


taxes = {
    'UT': Decimal('6.85'),
    'NV': Decimal('8'),
    'TX': Decimal('6.25'),
    'AL': Decimal('4'),
    'CA': Decimal('8.25'),
}


Tax.objects.all().delete()

tax_objects = []
for state_code, tax_value in taxes.items():
    tax_objects.append(
        Tax(
            state_code=state_code,
            tax=tax_value,
        ),
    )

Tax.objects.bulk_create(tax_objects)
