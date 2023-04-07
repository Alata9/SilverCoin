from django import forms
from django.contrib.auth.models import User

from .models import *


class AddFormExpenseItem(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['expense']


class AddFormPayment(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].empty_label = ''
        self.fields['counterparty'].empty_label = ''

    class Meta:
        model = Payments
        fields = ['date', 'amount', 'counterparty', 'item', 'comments']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'Date'}),
            'amount': forms.NumberInput(attrs={'max_digits': 15, 'decimal_places': 2}),
            'comments': forms.Textarea(attrs={'cols': 60, 'rows': 2}),
        }


