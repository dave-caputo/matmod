from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from clients.models import Client
from .forms import AssessmentForm
from .models import Assessment


class AssessmentCreateView(generic.CreateView):
    form_class = AssessmentForm
    model = Assessment
    template_name = 'assess/create.html'
    success_url = reverse_lazy('clients:create')

    def get_initial(self):
        client = get_object_or_404(Client, id=self.kwargs['client_pk'])
        return {'client': client}


class AssessmentListView(generic.ListView):
    model = Assessment
    template_name = 'assess/list.html'
