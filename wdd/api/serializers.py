from rest_framework.serializers import ModelSerializer
from catalog.models import Device


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        extra_kwargs = {
            'device_type': {
                'source': 'get_device_type_display'
            }
        }
