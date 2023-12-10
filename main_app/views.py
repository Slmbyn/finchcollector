from django.shortcuts import render
from .models import Finch
from django.views.generic.edit import CreateView

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
# create fake finch data ( a list with dictionaries inside)
# then pass that data to allfinches page by including it as the 3rd parameter in the render