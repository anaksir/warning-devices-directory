from django.urls import path
from .views import DevicesView, NewDevicesView


app_name = 'api'

urlpatterns = [
    path('devices/', DevicesView.as_view(), name='devices'),
    path('devices_v2/', NewDevicesView.as_view(), name='new-devices')
]
