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

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related('client').filter(
            client__pk=self.kwargs['client_pk'])


class AssessmentDetailView(generic.DetailView):
    model = Assessment
    template_name = 'assess/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answer_list'] = self.object.answers.all()
        context['client_pk'] = self.kwargs['client_pk']
        return context


class AssessmentUpdateView(generic.UpdateView):
    model = Assessment
    template_name = 'assess/update.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('assess:update', kwargs={
            'client_pk': self.kwargs['client_pk'],
            'pk': self.kwargs['pk']})


class AssessmentDeleteView(generic.DeleteView):
    model = Assessment
    template_name = 'assess/delete.html'

    def get_success_url(self):
        return reverse('clients:detail', kwargs={
            'pk': self.kwargs['client_pk']})
