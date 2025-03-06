#from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView

class PublicationListView(ListView):
    model = Publication
    template_name = 'publications-list.html'
   

# Create your views here.
