from django import forms
from .models import Device
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'filter_form'
        self.helper.layout = Layout(
            Row(
                Column(
                    Fieldset(
                        'Radius',
                        'min_radius',
                        'max_radius',
                    ),
                    css_class='col-2'
                ),
                Column(
                    Fieldset(
                        'Coordinates',
                        'upper_left_corner',
                        'bottom_right_corner',
                    ),
                    css_class='col-2',
                ),
                Column(
                    Fieldset(
                        'Type filter',
                        'device_type',
                        'search',
                    ),
                    css_class='col-2',
                ),
            ),
            Submit('submit', 'Get Devices'),
        )
