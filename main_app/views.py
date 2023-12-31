from django.shortcuts import render, redirect
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

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
    # feeding_form is set to an instance of FeedingForm and then it’s passed to detail.html in the context along with the finch.
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {'finch':finch, 'feeding_form':feeding_form})

def add_feeding(request, finch_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it has the finch_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    # Always be sure to redirect instead of render if data has been changed in the database.
    return redirect('detail', finch_id=finch_id)


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

    