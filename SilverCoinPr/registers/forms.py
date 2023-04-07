from django import forms
from django.contrib.auth.models import User

from income.models import *
from payments.models import *
from subjects.models import *
from .models import *



# ------------------------------------ПОКА НЕ РАБОЧАЯ
class FilterForm(forms.Form):
    date_start = forms.DateField()
    date_end = forms.DateField()
    counterparty = forms.ModelChoiceField(queryset=Сounterparties.objects.all(), empty_label='')
    item_income = forms.ModelChoiceField(queryset=IncomeItem.objects.all(), empty_label='')
    item_expense = forms.ModelChoiceField(queryset=Expenses.objects.all(), empty_label='')


class FilterDateForm(forms.Form):
    year = forms.IntegerField(label='', required=False)


