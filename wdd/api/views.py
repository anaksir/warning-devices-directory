from rest_framework.generics import ListAPIView
from django_filters import rest_framework
from .serializers import DeviceSerializer
from catalog.models import Device


class DeviveFilterSet(rest_framework.FilterSet):
    class Meta:
        model = Device
        # fields = ('device_type', 'radius')

        fields = {
            'device_type': ['exact'],
            'radius': ['gte', 'lte'],
        }


class DevicesView(ListAPIView):
    '''
    Endpoint for list of all devices
    '''
    queryset = Device.objects.all().order_by('name')
    serializer_class = DeviceSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = {
        'device_type': ['exact'],
        'radius': ['gte', 'lte'],
    }
    # filterset_fields = ('device_type', 'radius')
