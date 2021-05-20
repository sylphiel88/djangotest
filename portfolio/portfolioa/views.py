from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name':'Jan'})

def projects(request):
    return render(request, 'projects.html')