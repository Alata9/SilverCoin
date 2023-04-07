from django.contrib import admin

from income.models import *
from payments.models import *


class СounterpartiesAdmin(admin.ModelAdmin):
    list_display = ['id', 'counterparty', 'user']
    list_display_links = ['id', 'counterparty']
    search_fields = ['counterparty', 'user']



class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'date', 'year', 'month', 'year_month', 'amount', 'counterparty', 'item', 'user']
    list_display_links = ['id', 'item']
    search_fields = ['date', 'counterparty', 'item', 'user']


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['id', 'expense', 'user']
    list_display_links = ['id', 'expense']
    search_fields = ['expense', 'user']


class IncomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'date', 'year', 'month', 'year_month', 'amount', 'counterparty', 'item', 'user']
    list_display_links = ['id', 'item']
    search_fields = ['date', 'counterparty', 'item', 'user']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

class IncomeItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'income_item', 'user']
    list_display_links = ['id', 'income_item']
    search_fields = ['income_item', 'user']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


admin.site.register(Сounterparties, СounterpartiesAdmin)
admin.site.register(IncomeItem, IncomeItemAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Payments, PaymentsAdmin)
