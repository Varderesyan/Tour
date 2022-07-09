from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Homebg
# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homs = Homebg.objects.all()
        return render(request, self.template_name, {'homs':homs}) 

class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)