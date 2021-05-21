from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    if 'color' in request.COOKIES.keys():
        color = request.COOKIES['color']
        color2 = request.COOKIES['color2']
    else:
        resp = HttpResponse('')
        color = '#9DCC1E'
        color2 = '#4F660F'
        resp.set_cookie('color',color)
        resp.set_cookie('color2',color2)
    return render(request, 'home.html', {'name':'Jan', 'color':color, 'color2':color2})

def projects(request):
    if 'color' in request.COOKIES.keys():
        color = request.COOKIES['color']
        color2 = request.COOKIES['color2']
    else:
        resp = HttpResponse('')
        color = '#ff0000'
        color2 = '#dd0000'
        resp.set_cookie('color',color)
        resp.set_cookie('color2',color2)
    return render(request, 'projects.html', {'color':color, 'color2':color2})
