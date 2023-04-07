from django.db import models

from registers.models import *
from subjects.models import *


class Expenses(models.Model):
    expense = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.expense

    class Meta:
        ordering = ['expense']

    def get_absolute_url(self):
        return '/reference'


class Payments(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, default='payments')
    year_month = models.CharField(max_length=255, blank=True)
    month = models.IntegerField(max_length=2, blank=True)
    year = models.IntegerField(max_length=4, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    counterparty = models.ForeignKey(Сounterparties, on_delete=models.PROTECT)
    item = models.ForeignKey(Expenses, on_delete=models.PROTECT)
    comments = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date}, {self.amount}, {self.counterparty}, {self.item}'

    class Meta:
        ordering = ['date', 'item']

    def get_absolute_url(self):
        return '/payment'