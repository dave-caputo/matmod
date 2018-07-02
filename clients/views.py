from django.urls import reverse_lazy
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
