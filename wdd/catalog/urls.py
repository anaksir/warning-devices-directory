"""URL for Catalog app."""
from django.urls import path

from .views import DevicesView


app_name = 'catalog'

urlpatterns = [
    path('devices/', DevicesView.as_view(), name='devices'),
]
