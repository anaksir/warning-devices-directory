# Generated by Django 3.2.4 on 2021-06-29 12:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Device name', max_length=20, unique=True)),
                ('device_type', models.CharField(choices=[('SI', 'Siren'), ('SP', 'Speaker')], help_text='Type of device', max_length=2)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8, validators=[django.core.validators.MinValueValidator(-90, message="Latitude can't be less than -90 degrees"), django.core.validators.MaxValueValidator(90, message="Latitude can't be more than 90 degrees")])),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, validators=[django.core.validators.MinValueValidator(-180, message="Longitude can't be less than -180 degrees"), django.core.validators.MaxValueValidator(180, message="Longitude can't be more than 180 degrees")])),
                ('address', models.CharField(db_index=True, max_length=100)),
                ('radius', models.PositiveIntegerField(help_text='Radius of coverage area (m)')),
            ],
        ),
    ]
