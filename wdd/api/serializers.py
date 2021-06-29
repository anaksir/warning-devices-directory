from rest_framework import serializers
from catalog.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    """
    Serializer for display a list of devices.
    Used in DevicesView.
    """
    coordinates = serializers.ReadOnlyField()

    class Meta:
        model = Device
        fields = ('name', 'device_type', 'radius', 'coordinates')
        extra_kwargs = {
            'device_type': {
                'source': 'get_device_type_display'
            }
        }
