import numpy
import pretty_html_table
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import Sum, Count
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, DateDetailView, CreateView, DetailView
from django.shortcuts import render, redirect
import pandas as pd
from unicodedata import decimal
from django.db.models import FloatField, F
from income.forms import AddFormIncomeItem
from income.models import *
from payments.forms import AddFormExpenseItem
from payments.models import *
from registers.forms import *
from subjects.forms import AddFormCounterparty
from subjects.models import Сounterparties
from django_pivot.pivot import pivot
from django_pandas.io import read_frame


menu = [
    {'title': 'Start', 'url_name': 'home', 'icons': ''},
    {'title': 'Reference books', 'url_name': 'reference', 'icons': '5_48x48.png'},
    {'title': 'Income', 'url_name': 'income', 'icons': '4_48x48.png'},
    {'title': 'Payments', 'url_name': 'payments', 'icons': '3_48x48.png'},
    {'title': 'Reports', 'url_name': 'reports', 'icons': '2_48x48.png'},
    {'title': 'Diagrams', 'url_name': 'diagrams', 'icons': '6_48x48.png'},
]

menu_invisible = [
    {'title': 'Login', 'url_name': 'login'},
    {'title': 'Sign in', 'url_name': 'signin'},
    {'title': 'Success', 'url_name': 'success'},
]


note = [
    'Step 1. Create lists of counterparties and items of income and expenses',
    'Step 2: Record your income here',
    'Step 3. Write down your expenses every day',
    'Step 4. Look at the reports using different filters',
    'Step 5: Analyze data through visual charts'
]



def MainView(request):
    context = {'menu': menu,
               'title': menu[0].get('title'),
               }
    return render(request, 'registers/index.html', context=context)

def InstructionView(request):
    context = {'menu': menu,
               'title': 'Instruction',
               }
    return render(request, 'registers/instruction.html', context=context)



@login_required
def ReferenceView(request):
    if request.user.id != None:
        pay_item = Expenses.objects.filter(user=request.user)
        income_item = IncomeItem.objects.filter(user=request.user)
        counterparties = Сounterparties.objects.filter(user=request.user)

    else:
        demo = User.objects.get(username='demo')
        pay_item = Expenses.objects.filter(user=demo)
        income_item = IncomeItem.objects.filter(user=demo)
        counterparties = Сounterparties.objects.filter(user=demo)

    if request.method == 'POST' and 'btn_save_counterparty' in request.POST:
        form1 = AddFormCounterparty(request.POST)
        if form1.is_valid():
            try:
                form1 = form1.save(commit=False)
                form1.user = request.user
                form1.save()
                return redirect('reference')
            except:
                form1.add_error(None, 'Data save error')
    else:
        form1 = AddFormCounterparty()

    if request.method == 'POST' and 'btn_save_income' in request.POST:
        form2 = AddFormIncomeItem(request.POST)
        if form2.is_valid():
            try:
                form2 = form2.save(commit=False)
                form2.user = request.user
                form2.save()
                return redirect('reference')
            except:
                form2.add_error(None, 'Data save error')
    else:
        form2 = AddFormIncomeItem()

    if request.method == 'POST' and 'btn_save_expense' in request.POST:
        form3 = AddFormExpenseItem(request.POST)
        if form3.is_valid():
            try:
                form3 = form3.save(commit=False)
                form3.user = request.user
                form3.save()
                return redirect('reference')
            except:
                form3.add_error(None, 'Data save error')
    else:
        form3 = AddFormExpenseItem()

    context = {'menu': menu,
               'pay_item': pay_item,
               'income_item': income_item,
               'counterparties': counterparties,
               'form1': form1,
               'form2': form2,
               'form3': form3,
               'title': menu[1].get('title'),
               'note': note[0],
               'icons': menu[1].get('icons'),
               }
    return render(request, 'registers/reference.html', context=context)


def ReportsView(request):
    if request.user.id != None:
        user = request.user
    else:
        user = User.objects.get(username='demo')

    qs_i = Income.objects.filter(user=user).values('type', 'item__income_item', 'amount', 'year_month')
    qs_p = Payments.objects.filter(user=user).values('type', 'item__expense', 'amount', 'year_month')

    if request.method == 'GET' and 'btn_show' in request.GET:
        form = FilterDateForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['year']:
                year = form.cleaned_data['year']
                qs_i = qs_i.filter(year=year)
                qs_p = qs_p.filter(year=year)
    else:
        form = FilterDateForm()

    data_i = pd.DataFrame(qs_i)
    data_p = pd.DataFrame(qs_p)
    data_i = data_i.rename(columns={'item__income_item': 'item'})
    data_p = data_p.rename(columns={'item__expense': 'item'})

    if not data_p.empty:
        data_p['amount'] = data_p['amount'].apply(lambda x: x*-1)

    if not data_p.empty or not data_i.empty:
        frames = [data_i, data_p]
        result = pd.concat(frames)
        result = result.sort_values(by='type')
        result = result.reset_index(drop=True)

        df = pd.pivot_table(result, index=['type', 'item'], columns='year_month', values='amount',
                        aggfunc='sum', margins=True, fill_value=0)
        df = pd.DataFrame(df)
        data = df.to_html()

    else:
        data = 'Data is empty'

    context = {'menu': menu,
               'data': data,
               'title': menu[4].get('title'),
               'form': FilterDateForm(),
               'note': note[3],
               'icons': menu[4].get('icons'),
               }
    return render(request, 'registers/reports.html', context=context)


def DiagramsView(request):
    if request.user.id != None:
        user = request.user
    else:
        user = User.objects.get(username='demo')

    qs_i = Income.objects.filter(user=user).values('month', 'item__income_item', 'amount')
    qs_p = Payments.objects.filter(user=user).values('month', 'item__expense', 'amount')

    if request.method == 'GET' and 'btn_show' in request.GET:
        form = FilterDateForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['year']:
                year = form.cleaned_data['year']
                qs_i = qs_i.filter(year=year)
                qs_p = qs_p.filter(year=year)
    else:
        form = FilterDateForm()

    data_i = pd.DataFrame(qs_i)
    data_p = pd.DataFrame(qs_p)
    data_i = data_i.rename(columns={'item__income_item': 'item'})
    data_p = data_p.rename(columns={'item__expense': 'item'})

    data_income_columns = pd.pivot_table(data_i, index='item', columns='month', values='amount', aggfunc='sum', fill_value=0)
    data_payments_columns = pd.pivot_table(data_i, index='item', columns='month', values='amount', aggfunc='sum', fill_value=0)
    # data_income_columns['Month'] = data_income_columns.index
    data_income_columns = data_income_columns.values.tolist()
    # data_payments_columns['Month'] = data_payments_columns.index
    data_payments_columns = data_payments_columns.values.tolist()
    print(data_income_columns)
    print(data_payments_columns)

# база для круговой и гистограммы доходы

    data_in = Income.objects.filter(user=user)
    data_income = {}
    for d in data_in:
        item = str(d.item)
        amount = float(d.amount)

        if item not in data_income:
                data_income[item] = amount
        else:
                data_income[item] += amount
    data_income = list(map(list, list(zip(list(data_income), list(data_income.values())))))

    # база для круговой и гистограммы расходы

    data_out = Payments.objects.filter(user=user)
    data_payments = {}
    for d in data_out:
        item = str(d.item)
        amount = float(d.amount)

        if item not in data_payments:
            data_payments[item] = amount
        else:
            data_payments[item] += amount
    data_payments = list(map(list, list(zip(list(data_payments), list(data_payments.values())))))




    context = {'menu': menu,
               "data_income": data_income,
               "data_payments": data_payments,
               "data_income_columns": data_income_columns,
               "data_payments_columns": data_payments_columns,
               "form": FilterDateForm(),
               'title': menu[5].get('title'),
               'note': note[4],
               'icons': menu[5].get('icons'),
               }
    return render(request, 'registers/diagrams.html', context=context)





