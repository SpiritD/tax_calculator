from django.db import models


class Tax(models.Model):
    """Налог по штатам."""

    state_code = models.CharField(
        primary_key=True,
        max_length=5,
    )
    state_name = models.CharField(
        max_length=30,
        default='',
    )
    tax = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )

    class Meta:
        db_table = 'state_taxes'
        ordering = ('state_code',)
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxes'
