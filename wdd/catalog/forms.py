from django import forms
from .models import Device
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset


class DeviceFilterForm(forms.Form):
    min_radius = forms.IntegerField(required=False)
    max_radius = forms.IntegerField(required=False)

    blank_choice = [('', '---------')]
    device_type = forms.ChoiceField(
        choices=blank_choice + Device.DeviceType.choices,
        required=False,
    )
    search = forms.CharField(
        required=False,
        help_text='Search in name and addess',
        widget=forms.TextInput(
            attrs={'placeholder': 'Search in name and addess fields'}
        )
    )
    upper_left_corner = forms.CharField(
        required=False,
    )
    bottom_right_corner = forms.CharField(
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'filter_form'
        self.helper.layout = Layout(
            Row(
                Column(
                    Fieldset(
                        'Radius filter',
                        'min_radius',
                        'max_radius',
                    ),
                    css_class='col-2'
                ),
                Column(
                    Fieldset(
                        'Coordinates filter',
                        'upper_left_corner',
                        'bottom_right_corner',
                    ),
                    css_class='col-2',
                ),
                Column(
                    Fieldset(
                        'Search filter',
                        'search',
                    ),
                    css_class='col-4',
                ),
            ),
            Submit('submit', 'Get Devices'),
        )
