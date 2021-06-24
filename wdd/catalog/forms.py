from django import forms
from .models import Device


class DeviceFilterForm(forms.Form):
    min_radius = forms.IntegerField(required=False)
    max_radius = forms.IntegerField(required=False)

    blank_choice = [('', '---------')]
    device_type = forms.ChoiceField(
        choices=blank_choice + Device.DeviceType.choices,
        required=False,
    )
