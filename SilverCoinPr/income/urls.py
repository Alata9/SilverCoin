from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('income/', IncomeView, name='income'),
    path('income_item/<int:pk>', IncomeItemUpdateView.as_view(), name='income_item_detail'),
    path('<int:pk>/income_item_delete', IncomeItemDeleteView.as_view(), name='income_item_delete'),
    path('income/<int:pk>', IncomeUpdateView.as_view(), name='income_detail'),
    path('<int:pk>/income_delete', IncomeDeleteView.as_view(), name='income_delete'),
]