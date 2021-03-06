from catalog.models import Device

from rest_framework import serializers


class DeviceSerializer(serializers.ModelSerializer):
    """
    Serializer for display a list of devices.

    Used in DevicesView.
    """

    coordinates = serializers.ReadOnlyField()

    class Meta:
        model = Device
        fields = ('name', 'device_type', 'radius', 'coordinates', 'address')
        extra_kwargs = {
            'device_type': {
                'source': 'get_device_type_display'
            }
        }
