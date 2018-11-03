from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import QreForm
from .models import Qre


class QreCreateView(generic.CreateView):
    form_class = QreForm
    model = Qre
    template_name = 'qres/create.html'
    success_url = reverse_lazy('qres:create')


class QreListView(generic.ListView):
    model = Qre
    template_name = 'qres/list.html'


class QreDetailView(generic.DetailView):
    model = Qre
    template_name = 'qres/detail.html'


class QreRenameView(generic.UpdateView):
    model = Qre
    template_name = 'qres/qre_rename.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('qres:rename', kwargs={'pk': self.kwargs['pk']})


class QreDeleteView(generic.DeleteView):
    model = Qre
    template_name = 'qres/delete.html'
    success_url = reverse_lazy('dashboard:index')
