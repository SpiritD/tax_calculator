from django.contrib import admin

from calculator.models import (
    Discount,
    Tax,
)


admin.site.register(Discount)
admin.site.register(Tax)
