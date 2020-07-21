from django.shortcuts import render, get_object_or_404, redirect
from .models import codes
from .forms import CodeForm
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class CodeListView(ListView):
    model = codes

    def get_queryset(self):
        return codes.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class CodeDetailView(DetailView):
    model = codes

class CodeCreateView(CreateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'basic/code_detail.html'
    form_class = CodeForm
    model = codes

class CodeUpdateView(UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'basic/code_detail.html'
    form_class = CodeForm
    model = codes

class CodeDeleteView(DeleteView, LoginRequiredMixin):
    model = codes
    success_url = reverse_lazy('code_list')

class DraftListView(ListView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'basic/code_detail.html'
    model = codes

    def get_queryset(self):
        return codes.objects.filter(published_date__isnull = True).order_by('created_date')

@login_required
def codes_publish(request, pk):
    code = get_object_or_404(codes, pk = pk)
    code.publish()
    return redirect('code_detail', pk = pk)