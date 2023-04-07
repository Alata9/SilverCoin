from datetime import date
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from registers.views import *
from .forms import *
from .models import *

@login_required
def IncomeView(request):
    if request.user.id != None:
        user = request.user
    else:
        user = User.objects.get(username='demo')

    income = Income.objects.filter(user=user)
    data_item = IncomeItem.objects.filter(user=user)
    data_counterparty = Сounterparties.objects.filter(user=user)

    form = IncomeFilter(request.GET)
    if form.is_valid():
        if form.cleaned_data['date']:
            income = income.filter(date__gte=form.cleaned_data['date'])
        if form.cleaned_data['date_end']:
            income = income.filter(date__lte=form.cleaned_data['date_end'])
        if form.cleaned_data['counterparty']:
            income = income.filter(counterparty=form.cleaned_data['counterparty'])
        if form.cleaned_data['item']:
            income = income.filter(item=form.cleaned_data['item'])


    if request.method == 'POST' and 'btn_create' in request.POST:
        form = AddFormIncome(request.POST, request.user)

        if form.is_valid():
            try:
                form = form.save(commit=False)
                form.user = request.user
                form.year = form.date.year
                form.month = form.date.month
                form.year_month = str(form.date.year) + ' - ' + str(form.date.month)
                form.save()
                return redirect('income')
            except:
                form.add_error(None, 'Data save error')
    else:
        form = AddFormIncome()

    context = {
               'menu': menu,
               'form_add': AddFormIncome(),
               'form_filter': IncomeFilter(),
               'title': menu[2].get('title'),
               'note': note[1],
               'income': income,
               'data_item': data_item,
               'data_counterparty': data_counterparty,
               'icons': menu[2].get('icons'),
               }

    return render(request, 'income/income.html', context=context)


# ----------------------- РЕДАКТИРОВАНИЕ

class IncomeItemUpdateView(UpdateView):
    model = IncomeItem
    template_name = 'income/income_item_detail.html'

    form_class = AddFormIncomeItem


class IncomeUpdateView(UpdateView):
    model = Income
    template_name = 'income/income_detail.html'

    form_class = AddFormIncome



# ----------------------- УДАЛЕНИЕ

class IncomeItemDeleteView(DeleteView):
    error = ''
    model = IncomeItem
    success_url = '/reference'
    template_name = 'income/income_item_delete.html'

    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError:

            self.object = self.get_object()
            context = self.get_context_data(
                object=self.object,
                error="Any error msg"
            )
            return self.render_to_response(context)


class IncomeDeleteView(DeleteView):
    error = ''
    model = Income
    success_url = '/income'
    template_name = 'income/income_delete.html'


