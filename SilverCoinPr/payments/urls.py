from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('payment/', PaymentsView, name='payments'),
    path('expenses_item/<int:pk>', ExpensesItemUpdateView.as_view(), name='expenses_detail'),
    path('<int:pk>/expenses_delete', ExpensesItemDeleteView.as_view(), name='expenses_delete'),
    path('payment/<int:pk>', PaymentUpdateView.as_view(), name='payment_detail'),
    path('<int:pk>/payment_delete', PaymentDeleteView.as_view(), name='payment_delete'),

]