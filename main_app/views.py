from django.shortcuts import render
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def allfinches (request):
    finch = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finch
    })

def finch_detail (request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch':finch})

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    # success_url = '/allfinches/{finch.id}'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'age', 'color']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/allfinches'

    