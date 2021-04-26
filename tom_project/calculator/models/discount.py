from django.db import models


class Discount(models.Model):
    """Скидка в зависимости от стоимости."""

    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )
    discount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    class Meta:
        db_table = 'discounts'
        ordering = ('-cost',)
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'
