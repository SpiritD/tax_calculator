from django.shortcuts import render

from calculator.forms import CalculatorForm


def calculator_view(request):
    # Обработка пост запроса с параметрами
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        # проверяем параметры
        if form.is_valid():
            # вычисляем итоговую стоимость
            result = 5
            return render(
                request=request,
                template_name='calculator/home.html',
                context={'form': form, 'result': result},
            )

    # При гет запросе возвращаем пустую форму
    else:
        form = CalculatorForm()

    return render(request, 'calculator/home.html', {'form': form})
