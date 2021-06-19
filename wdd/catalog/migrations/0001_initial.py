# Generated by Django 3.2.4 on 2021-06-19 12:16

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
                ('name', models.CharField(help_text='Device name', max_length=20, unique=True)),
                ('device_type', models.CharField(choices=[('SI', 'Siren'), ('SP', 'Speaker')], help_text='Type of device', max_length=2)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('address', models.CharField(max_length=100)),
                ('radius', models.PositiveIntegerField(help_text='Radius of coverage area (m)')),
            ],
        ),
    ]
