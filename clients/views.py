from django.views import generic

from .models import Client


class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'clients/detail.html'
