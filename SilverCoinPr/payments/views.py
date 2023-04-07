from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render, redirect

from registers.views import menu, note
from .models import *
from .forms import *

@login_required
def PaymentsView(request):
    #-----------------проверка на авторизацию
    if request.user.id != None:
        pays = Payments.objects.filter(user=request.user)
    else:
        demo = User.objects.get(username='demo')
        pays = Payments.objects.filter(user=demo)

    if request.method == 'POST':
        form = AddFormPayment(request.POST)
        if form.is_valid():
            try:
                form = form.save(commit=False)
                form.user = request.user
                form.year_month = str(form.date.year) + ' - ' + str(form.date.month)
                form.month = form.date.month
                form.year = form.date.year
                form.save()
                return redirect('payments')
            except:
                form.add_error(None, 'Data save error')
    else:
        form = AddFormPayment()

    context = {'pays': pays,
               'menu': menu,
               'form': form,
               'title': menu[3].get('title'),
               'note': note[2],
               'icons': menu[3].get('icons'),
               }
    return render(request, 'payments/payment.html', context=context)


class ExpensesItemUpdateView(UpdateView):
    model = Expenses
    template_name = 'payments/expenses_detail.html'

    form_class = AddFormExpenseItem


class PaymentUpdateView(UpdateView):
    model = Payments
    template_name = 'payments/payment_detail.html'

    form_class = AddFormPayment


class ExpensesItemDeleteView(DeleteView):
    error = ''
    model = Expenses
    success_url = '/reference'
    template_name = 'payments/expenses_delete.html'


class PaymentDeleteView(DeleteView):
    error = ''
    model = Payments
    success_url = '/payment'
    template_name = 'payments/payment_delete.html'
