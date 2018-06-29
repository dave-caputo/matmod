from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import QreSectionForm
from .models import Qre, Section


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


class QreDeleteView(generic.DeleteView):
    model = Qre
    template_name = 'qres/delete.html'
    success_url = reverse_lazy('dashboard:index')


class SectionCreateView(generic.CreateView):
    model = Section
    template_name = 'qres/section_create.html'
    form_class = QreSectionForm
    success_url = reverse_lazy('qres:section_create')

    def get_initial(self):
        qre = get_object_or_404(Qre, id=self.kwargs['qre_id'])
        return {'qre': qre}

    from django.urls import reverse_lazy

    def get_success_url(self):
        return reverse('qres:section_create',
                       kwargs={'qre_id': self.kwargs['qre_id']})


class SectionListView(generic.ListView):
    model = Section
    template_name = 'qres/section_list.html'

    def get_queryset(self):
        return (
            Section.objects.select_related('qre')
            .filter(qre__id=self.kwargs['qre_id'])
        )
