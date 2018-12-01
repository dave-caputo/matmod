from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import QreForm
from .models import Qre


class QreCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = QreForm
    model = Qre
    template_name = 'qres/create.html'
    success_url = reverse_lazy('qres:create')

    def get_initial(self):
        initial = super().get_initial()
        initial['org'] = self.request.user.org
        return initial


class QreListView(LoginRequiredMixin, generic.ListView):
    model = Qre
    template_name = 'qres/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            qs.filter(org=self.request.user.org)


class QreDetailView(LoginRequiredMixin, generic.DetailView):
    model = Qre
    template_name = 'qres/detail.html'


class QreRenameView(LoginRequiredMixin, generic.UpdateView):
    model = Qre
    template_name = 'qres/qre_rename.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('qres:rename', kwargs={'pk': self.kwargs['pk']})


class QreDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Qre
    template_name = 'qres/delete.html'
    success_url = reverse_lazy('dashboard:index')
