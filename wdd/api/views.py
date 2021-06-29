from rest_framework import generics
from rest_framework import filters
from django_filters import rest_framework as dfrf
from .serializers import DeviceSerializer
from .pagination import MyPagination
from catalog.models import Device


class DevicesView(generics.ListAPIView):
    '''
    Endpoint for list of all devices
    '''
    queryset = Device.objects.all().order_by('id')
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


class NewDevicesView(generics.ListAPIView):
    '''
    New Endpoint for list of all devices without django-filters
    '''
    queryset = Device.objects.all().order_by('name')
    serializer_class = DeviceSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        queryset = Device.objects.all()

        return queryset
