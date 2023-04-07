from django.conf import settings
from django.db import models


from subjects.models import *


class IncomeItem(models.Model):
    income_item = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.income_item

    class Meta:
        ordering = ['income_item']

    def get_absolute_url(self):
        return '/reference'


class Income(models.Model):
    date = models.DateField(blank=True)
    type = models.CharField(max_length=10, default='income')
    year_month = models.CharField(max_length=15, blank=True)
    year = models.IntegerField(max_length=4, blank=True)
    month = models.IntegerField(max_length=2, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    counterparty = models.ForeignKey(Сounterparties, on_delete=models.PROTECT, blank=True)
    item = models.ForeignKey(IncomeItem, on_delete=models.PROTECT, blank=True)
    comments = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date}, {self.amount}, {self.counterparty}, {self.item}'

    class Meta:
        ordering = ['date', 'item']

    def get_absolute_url(self):
        return '/income'

    def get_year_month(self):
        year_month = str(self.date)[:8]
        return year_month