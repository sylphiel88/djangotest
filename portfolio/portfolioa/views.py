from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    if 'color' in request.COOKIES.keys() and 'color2' in request.COOKIES.keys() and 'colorbw' in request.COOKIES.keys():
        color = request.COOKIES['color']
        color2 = request.COOKIES['color2']
        colorbw = request.COOKIES['colorbw']
    else:
        resp = HttpResponse('')
        color = '#9DCC1E'
        color2 = '#4F660F'
        colorbw = '#FFFFFF'
        resp.set_cookie('color',color)
        resp.set_cookie('color2',color2)
        resp.set_cookie('color',colorbw)
    return render(request, 'home.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw})

def projects(request):
    if 'color' in request.COOKIES.keys() and 'color2' in request.COOKIES.keys() and 'colorbw' in request.COOKIES.keys():
        color = request.COOKIES['color']
        color2 = request.COOKIES['color2']
        colorbw = request.COOKIES['colorbw']
    else:
        resp = HttpResponse('')
        color = '#9DCC1E'
        color2 = '#4F660F'
        colorbw = '#FFFFFF'
        resp.set_cookie('color',color)
        resp.set_cookie('color2',color2)
        resp.set_cookie('color',colorbw)
    return render(request, 'projects.html', {'color':color, 'color2':color2, 'colorbw':colorbw})
