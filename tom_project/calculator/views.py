from django.shortcuts import render

from calculator.calculation import calculate_total_cost
from calculator.exceptions import StateNotFound
from calculator.forms import CalculatorForm
from calculator.repository import Repository


def calculator_view(request):
    # Обработка пост запроса с параметрами
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        # проверяем параметры
        if form.is_valid():
            # вычисляем итоговую стоимость
            try:
                total_cost = calculate_total_cost(
                    price=form.cleaned_data['price'],
                    quantity=form.cleaned_data['quantity'],
                    state_code=form.cleaned_data['state_code'],
                    repository=Repository(),
                )
            except StateNotFound:
                return render(
                    request=request,
                    template_name='calculator/home.html',
                    context={
                        'form': form,
                        'error': 'State not found',
                    },
                )

            return render(
                request=request,
                template_name='calculator/home.html',
                context={
                    'form': form,
                    'total_cost': total_cost,
                },
            )

    # При гет запросе возвращаем пустую форму
    else:
        form = CalculatorForm()

    return render(request, 'calculator/home.html', {'form': form})
