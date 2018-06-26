from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Qre


class QreCreateView(CreateView):
    model = Qre
    template_name = 'qres/create.html'
    fields = ['name']
    success_url = reverse_lazy('qres:create')


class QreListView(ListView):
    model = Qre
    template_name = 'qres/list.html'
