from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('counterparty/<int:pk>', CounterpartyUpdateView.as_view(), name='counterparty_detail'),
    path('<int:pk>/counterparty_delete', CounterpartyDeleteView.as_view(), name='counterparty_delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)