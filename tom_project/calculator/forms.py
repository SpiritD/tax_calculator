from django import forms


class CalculatorForm(forms.Form):
    """Форма для калькулятора."""

    quantity = forms.IntegerField(min_value=0)
    price = forms.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    state_code = forms.CharField(max_length=5)
