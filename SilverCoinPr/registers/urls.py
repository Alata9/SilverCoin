from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from .views import *

urlpatterns = [
    path('', MainView, name='home'),
    path('reference/', ReferenceView, name='reference'),
    path('reports/', ReportsView, name='reports'),
    path('diagrams/', DiagramsView, name='diagrams'),
    path('instruction/', InstructionView, name='instruction'),
    # path('error_delete/', ErrorDeleteView, name='error_delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
