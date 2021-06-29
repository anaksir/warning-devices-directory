from django.contrib import admin
from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'device_type',
        'radius',
        'coordinates',
        'address'
    )
    list_filter = ('device_type',)
