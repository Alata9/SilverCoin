

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import request

from .models import *

# -------------------------------------------form for create & update in reference/ IncomeItem
class AddFormIncomeItem(forms.ModelForm):
    class Meta:
        model = IncomeItem
        fields = ['income_item']


# --------------------------------------------form for create & update in income/ Income
class AddFormIncome(forms.ModelForm):

    class Meta:
        model = Income
        fields = ['date', 'amount', 'counterparty', 'item', 'comments']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'Date'}),
            'amount': forms.NumberInput(attrs={'max_digits': 15, 'decimal_places': 2}),
            'comments': forms.Textarea(attrs={'cols': 60, 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].empty_label = ''
        self.fields['counterparty'].empty_label = ''
        self.fields['counterparty'].queryset = Сounterparties.objects.filter(user=3)        # фильтр по user сделать
        self.fields['item'].queryset = IncomeItem.objects.filter(user=3)                    # фильтр по user сделать


# --------------------------------------------form for filter in income/ Income
class IncomeFilter(forms.ModelForm):
    date_end = forms.DateField(required=False)                                              # добавить в поле ввода календарь
    class Meta:
        model = Income
        fields = ['counterparty', 'item', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'Date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].empty_label = ''
        self.fields['counterparty'].empty_label = ''
        self.fields['counterparty'].queryset = Сounterparties.objects.filter(user=3)        # фильтр по user сделать
        self.fields['item'].queryset = IncomeItem.objects.filter(user=3)                    # фильтр по user сделать
        self.fields['date'].label = ''
        self.fields['date_end'].label = ''
