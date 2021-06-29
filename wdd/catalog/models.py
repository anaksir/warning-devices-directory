from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Device(models.Model):
    '''
    Модель устройства оповещения
    '''
    class DeviceType(models.TextChoices):
        SIREN = ('SI', 'Siren')
        SPEAKER = ('SP', 'Speaker')

    name = models.CharField(
        max_length=20,
        unique=True,
        help_text='Device name',
        db_index=True,
    )

    device_type = models.CharField(
        max_length=2,
        choices=DeviceType.choices,
        help_text='Type of device'
    )

    latitude = models.DecimalField(
        max_digits=8,
        decimal_places=6,
        validators=[
            MinValueValidator(
                -90,
                message="Latitude can't be less than -90 degrees"
            ),
            MaxValueValidator(
                90,
                message="Latitude can't be more than 90 degrees"
            ),
        ]
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        validators=[
            MinValueValidator(
                -180,
                message="Longitude can't be less than -180 degrees"
            ),
            MaxValueValidator(
                180,
                message="Longitude can't be more than 180 degrees"
            ),
        ]
    )

    address = models.CharField(
        max_length=100,
        db_index=True,
    )

    radius = models.PositiveIntegerField(
        help_text='Radius of coverage area (m)'
    )

    @property
    def coordinates(self) -> str:
        return f'{self.latitude}, {self.longitude}'

    def __str__(self) -> str:
        return f'{self.name} ({self.get_device_type_display()})'
