from django.urls import path

from .views import DevicesView


app_name = 'api'

urlpatterns = [
    path('devices/', DevicesView.as_view(), name='devices'),
]
