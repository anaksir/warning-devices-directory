from catalog.models import Device

from django.db.models import Q

from django_filters import rest_framework as dfrf

from rest_framework import filters, generics

from .pagination import MyPagination
from .serializers import DeviceSerializer


class DevicesView(generics.ListAPIView):
    """Endpoint for list of all devices use django_filters."""

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


class DevicesViewWithoutDF(generics.ListAPIView):
    """Endpoint for list of all devices without django_filters."""

    serializer_class = DeviceSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        """Return filtred queryset."""
        queryset = Device.objects.all().order_by('name')

        device_type_param = self.request.query_params.get('device_type')
        max_radius = self.request.query_params.get('radius__lte')
        min_radius = self.request.query_params.get('radius__gte')
        search = self.request.query_params.get('search')
        min_latitude = self.request.query_params.get('latitude__gte')
        max_latitude = self.request.query_params.get('latitude__lte')
        min_longitude = self.request.query_params.get('longitude__gte')
        max_longitude = self.request.query_params.get('longitude__lte')
        coordinates = (
            min_latitude,
            max_latitude,
            min_longitude,
            max_longitude
        )

        filter_conditions = Q()
        if device_type_param:
            filter_conditions &= Q(device_type__exact=device_type_param)

        if max_radius is not None:
            filter_conditions &= Q(radius__lte=max_radius)

        if min_radius is not None:
            filter_conditions &= Q(radius__gte=min_radius)

        if search is not None:
            filter_conditions &= (Q(name__icontains=search) |
                                  Q(address__icontains=search))

        if all(coord is not None for coord in coordinates):
            filter_conditions &= (
                Q(latitude__gte=min_latitude) &
                Q(latitude__lte=max_latitude) &
                Q(longitude__gte=min_longitude) &
                Q(longitude__lte=max_longitude)
            )

        queryset = queryset.filter(filter_conditions)
        return queryset
