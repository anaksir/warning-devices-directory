from django.views.generic import TemplateView
from .forms import DeviceFilterForm


class DevicesView(TemplateView):
    template_name = 'catalog/devices_crispy_v2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = DeviceFilterForm()
        context['form'] = form
        return context
