from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import bewertung
from .forms import aqbw
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
    bws = bewertung.objects.all()
    i=0
    sumbw1=0
    sumbw2=0
    sumbw3=0
    for bewertungen in bws:
        bw1wert = bewertungen.bw1
        bw2wert = bewertungen.bw2
        bw3wert = bewertungen.bw3
        sumbw1 += bw1wert
        sumbw2 += bw2wert
        sumbw3 += bw3wert
        i = i + 1
    lenbw = len(bws)
    anmtext = bewertung.objects.get(id=lenbw).anm
    avgbw1 = round(sumbw1 / i, 1)
    avgbw2 = round(sumbw2 / i, 1)
    avgbw3 = round(sumbw3 / i, 1)
    if request.method == 'POST':
        sendbw1 = int(request.POST['bw1'])
        sendbw2 = int(request.POST['bw2'])
        sendbw3 = int(request.POST['bw3'])
        sendanm = request.POST['anm']
        b = bewertung.objects.all().create(bw1=sendbw1, bw2=sendbw2, bw3=sendbw3, anm=sendanm)
        return redirect('aqbewe')
    form = aqbw()
    return render(request, 'bewertungaq.html', {'bw1':avgbw1, 'bw2':avgbw2, 'bw3':avgbw3,'anm':anmtext, 'form':form})

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