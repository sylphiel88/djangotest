from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    zahl = 2 + 6
    return render(request, 'home.html', {'name':zahl})

def projects(request):
    return render(request, 'projects.html')