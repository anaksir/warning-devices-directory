from django.db import models


class Device(models.Model):
    '''
    Модель устройства оповещения
    '''
    class DeviceType(models.TextChoices):
        SIREN = 'SI', 'Siren'
        SPEAKER = 'SP', 'Speaker'

    name = models.CharField(
        max_length=20,
        unique=True,
        help_text='Device name')

    device_type = models.CharField(
        max_length=2,
        choices=DeviceType.choices,
        help_text='Type of device'
    )

    latitude = models.DecimalField(
        max_digits=8,
        decimal_places=6)

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6)

    address = models.CharField(
        max_length=100,
    )

    radius = models.PositiveIntegerField(
        help_text='Radius of coverage area (m)'
    )
