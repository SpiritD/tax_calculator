from django.shortcuts import render

from calculator.forms import CalculatorForm
from django.views.generic.edit import FormView


class CalculatorView(FormView):
    """Вьюха для главной страницы калькулятора"""
    template_name = 'calculator/home.html'
    form_class = CalculatorForm

    def form_valid(self, form):
        """Проверка полей, если нужно."""

        return super().form_valid(form)


def calculator(request):
    ...


def calculator_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CalculatorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            result = 5
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(
                request=request,
                template_name='calculator/home.html',
                context={'form': form, 'result': result},
            )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CalculatorForm()

    return render(request, 'calculator/home.html', {'form': form})
