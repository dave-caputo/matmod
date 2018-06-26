from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Qre


class QreCreateView(generic.CreateView):
    model = Qre
    template_name = 'qres/create.html'
    fields = ['name']
    success_url = reverse_lazy('qres:create')


class QreListView(generic.ListView):
    model = Qre
    template_name = 'qres/list.html'


class QreDetailView(generic.DetailView):
    model = Qre
    template_name = 'qres/detail.html'


class QreUpdateView(generic.UpdateView):
    model = Qre
    template_name = 'qres/update.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('qres:update', kwargs={'pk': self.kwargs['pk']})
