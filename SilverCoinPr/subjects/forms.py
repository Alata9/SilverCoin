from django import forms
from django.contrib.auth.models import User

from .models import *



class AddFormCounterparty(forms.ModelForm):
    class Meta:
        model = Сounterparties
        fields = ['counterparty']
        widgets = {
            'select': forms.CheckboxInput(),
        }