from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snacks

class SnacksListView(ListView):
    template_name = 'snack_list.html'
    model = Snacks
    context_object_name = 'snacks'

class SnacksDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snacks
   