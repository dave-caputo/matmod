from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from questionnaires.models import Qre
from .forms import SectionForm
from .models import Section


class SectionCreateView(generic.CreateView):
    form_class = SectionForm
    model = Section
    template_name = 'sections/create.html'
    success_url = reverse_lazy('sections:create')

    def get_initial(self):
        qre = get_object_or_404(Qre, id=self.kwargs['qre_pk'])
        return {'qre': qre}

    def get_success_url(self):
        return reverse('sections:create',
                       kwargs={'qre_pk': self.kwargs['qre_pk']})


class SectionListView(generic.ListView):
    model = Section
    template_name = 'sections/list.html'

    def get_queryset(self):
        return (
            Section.objects.select_related('qre')
            .filter(qre__id=self.kwargs['qre_pk'])
        )


class SectionMoveView(generic.UpdateView):
    '''
    Move section up or down in the qre by updating the order field
    using the Ordered Model 'up' and 'down' methods.
    '''
    model = Section
    fields = []

    def form_valid(self, form):

        direction = self.kwargs.get('direction')  # Accepts str 'up' or 'down'
        self.object = form.save()
        getattr(self.object, direction)()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('sections:list',
                       kwargs={'qre_pk': self.kwargs['qre_pk']})


class SectionDetailView(generic.DetailView):
    model = Section
    template_name = 'sections/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_list'] = self.object.questions.all()
        return context


class SectionUpdateView(generic.UpdateView):
    model = Section
    template_name = 'sections/update.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('sections:update', kwargs={
            'qre_pk': self.kwargs['qre_pk'],
            'pk': self.kwargs['pk']
        })


class SectionDeleteView(generic.DeleteView):
    model = Section
    template_name = 'sections/delete.html'

    def get_success_url(self):
        return reverse('qres:detail', kwargs={'pk': self.kwargs['qre_pk']})
