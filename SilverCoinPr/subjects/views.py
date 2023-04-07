from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render, redirect

from .models import *
from .forms import *


class CounterpartyDeleteView(DeleteView):
    error = ''
    model = Сounterparties
    success_url = '/reference'
    template_name = 'subjects/counterparty_delete.html'


class CounterpartyUpdateView(UpdateView):
    model = Сounterparties
    template_name = 'subjects/counterparty_detail.html'

    form_class = AddFormCounterparty