from catalog.models import Device

from django_filters import rest_framework as dfrf

from rest_framework import filters, generics

from .pagination import MyPagination
from .serializers import DeviceSerializer


class DevicesView(generics.ListAPIView):
    '''
    Endpoint for list of all devices
    '''
    queryset = Device.objects.all().order_by('name')
    serializer_class = DeviceSerializer
    filter_backends = [
        dfrf.DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = {
        'device_type': ['exact'],
        'radius': ['gte', 'lte'],
        'latitude': ['gte', 'lte'],
        'longitude': ['gte', 'lte'],
    }
    search_fields = ['name', 'address']
    pagination_class = MyPagination
