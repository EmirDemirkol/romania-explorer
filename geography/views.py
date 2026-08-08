from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Area, Attraction

class GeographyView(ListView):
    model = Area
    template_name = 'geography/geography.html'
    context_object_name = 'areas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attractions'] = Attraction.objects.all()
        return context

class AreaListView(ListView):
    model = Area
    template_name = 'geography/area_list.html'
    context_object_name = 'areas'

class AreaDetailView(DetailView):
    model = Area
    template_name = 'geography/area_detail.html'

class AreaCreateView(CreateView):
    model = Area
    fields = ['name', 'area_type']
    template_name = 'geography/area_form.html'
    success_url = reverse_lazy('geography:area_list')

class AreaUpdateView(UpdateView):
    model = Area
    fields = ['name', 'area_type']
    template_name = 'geography/area_form.html'
    success_url = reverse_lazy('geography:area_list')

class AreaDeleteView(DeleteView):
    model = Area
    template_name = 'geography/area_confirm_delete.html'
    success_url = reverse_lazy('geography:area_list')

class AttractionListView(ListView):
    model = Attraction
    template_name = 'geography/attraction_list.html'
    context_object_name = 'attractions'

class AttractionDetailView(DetailView):
    model = Attraction
    template_name = 'geography/attraction_detail.html'

class AttractionCreateView(CreateView):
    model = Attraction
    fields = ['name', 'area', 'description', 'image']
    template_name = 'geography/attraction_form.html'
    success_url = reverse_lazy('geography:attraction_list')

class AttractionUpdateView(UpdateView):
    model = Attraction
    fields = ['name', 'area', 'description', 'image']
    template_name = 'geography/attraction_form.html'
    success_url = reverse_lazy('geography:attraction_list')

class AttractionDeleteView(DeleteView):
    model = Attraction
    template_name = 'geography/attraction_confirm_delete.html'
    success_url = reverse_lazy('geography:attraction_list')
