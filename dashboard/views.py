from django.contrib.sites.models import Site
from django.views.generic import TemplateView

from .utils import get_assess_list, get_client_list, get_qre_list


class DashboardIndexView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['client_list'] = get_client_list()
        context['qre_list'] = get_qre_list()
        context['recent_assess_list'] = get_assess_list()[:10]
        context['site'] = Site.objects.get_current()

        return context
