from django import forms
from .models import Device


class DeviceFilterForm(forms.Form):
    min_radius = forms.IntegerField(
        required=False,
        help_text='integer in meters'
    )
    max_radius = forms.IntegerField(
        required=False,
        help_text='integer in meters'
    )

    blank_choice = [('', '---------')]
    device_type = forms.ChoiceField(
        choices=blank_choice + Device.DeviceType.choices,
        required=False,
        help_text='Select device type'
    )
    search = forms.CharField(
        required=False,
        help_text='Search in name and addess',
        widget=forms.TextInput(
            attrs={'placeholder': 'Search text'}
        )
    )
    upper_left_corner = forms.CharField(
        help_text='Enter coordinates',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'latitude, longitude'}
        )
    )
    bottom_right_corner = forms.CharField(
        required=False,
        help_text='Enter coordinates',
        widget=forms.TextInput(
            attrs={'placeholder': 'latitude, longitude'}
        )
    )
