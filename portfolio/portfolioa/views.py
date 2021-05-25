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

def werdegang(request):
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
    return render(request, 'werdegang.html', {'color':color, 'color2':color2, 'colorbw':colorbw})

def schule(request):
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
    return render(request, 'schule.html', {'color':color, 'color2':color2, 'colorbw':colorbw})

def hobbies(request):
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
    return render(request, 'hobbies.html', {'color':color, 'color2':color2, 'colorbw':colorbw})

def aqindex(request):
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
    return render(request, 'parallaxpics.html', {'color':color, 'color2':color2, 'colorbw':colorbw})

def aqbewe(request):
    return render(request, 'bewertungaq.html')

def aquarium1(request):
    return render(request, 'aquarium1.html')

def aquarium2(request):
    return render(request, 'aquarium2.html')

def aquarium3(request):
    return render(request, 'aquarium3.html')

def technik(request):
    return render(request, 'technik.html')

def gallery(request):
    return render(request, 'gallery.html')