from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import ClientForm
from .models import Client


class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ClientForm
    model = Client
    template_name = 'clients/create.html'
    success_url = reverse_lazy('clients:create')

    def get_initial(self):
        initial = super().get_initial()
        initial['org'] = self.request.user.org
        return initial


class ClientListView(generic.ListView):
    model = Client
    template_name = 'clients/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            qs.filter(org=self.request.user.org, id=self.request.user.client.id)


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Client
    template_name = 'clients/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assessment_list'] = self.object.assessments.all()
        return context


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Client
    template_name = 'clients/update.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('clients:update', kwargs={'pk': self.kwargs['pk']})


class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Client
    template_name = 'clients/delete.html'
    success_url = reverse_lazy('dashboard:index')
