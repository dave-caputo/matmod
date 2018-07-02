from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Client


class ClientCreateView(generic.CreateView):
    model = Client
    template_name = 'clients/create.html'
    fields = ['name', ]
    success_url = reverse_lazy('clients:create')


class ClientListView(generic.ListView):
    model = Client
    template_name = 'clients/list.html'


class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'clients/detail.html'


class ClientUpdateView(generic.UpdateView):
    model = Client
    template_name = 'clients/update.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('clients:update', kwargs={'pk': self.kwargs['pk']})


class ClientDeleteView(generic.DeleteView):
    model = Client
    template_name = 'clients/delete.html'
    success_url = reverse_lazy('dashboard:index')
