from django.db import models
from django_registration.forms import User


class Сounterparties(models.Model):
    counterparty = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.counterparty

    class Meta:
        ordering = ['counterparty']

    def get_absolute_url(self):
        return '/reference'
