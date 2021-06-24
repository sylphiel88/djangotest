from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import bewertung
from .models import video
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
    rubix = video.objects.all().get(pk=4)
    maxit = video.objects.all().get(pk=5)
    return render(request, 'home.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit})

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
    rubix = video.objects.all().get(pk=4)
    maxit = video.objects.all().get(pk=5)
    return render(request, 'projects.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit})

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
    rubix = video.objects.all().get(pk=4)
    maxit = video.objects.all().get(pk=5)
    return render(request, 'werdegang.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit})

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
    rubix = video.objects.all().get(pk=4)
    maxit = video.objects.all().get(pk=5)
    return render(request, 'schule.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit})

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
    rubix = video.objects.all().get(pk=4)
    maxit = video.objects.all().get(pk=5)
    return render(request, 'hobbies.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit})

def anschreiben(request):
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
    rubix = video.objects.all().get(pk=4)
    maxit = video.objects.all().get(pk=5)
    return render(request, 'anschreiben.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit})

def ziele(request):
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
    rubix = video.objects.all().get(pk=4)
    maxit = video.objects.all().get(pk=5)
    return render(request, 'ziele.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit})

def bewertungns(request):
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
    return render(request, 'bewertung.html', {'color':color, 'color2':color2, 'colorbw':colorbw})

def videos(request):
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
    videodb = video.objects.all()
    rubix = video.objects.all().get(pk=4)
    maxit = video.objects.all().get(pk=5)    
    return render(request, 'videos.html', {'color':color, 'color2':color2, 'colorbw':colorbw, 'videos': videodb, 'rubix':rubix, 'maxit':maxit})

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

def impressum(request):
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
    rubix = video.objects.all().get(pk=4)
    maxit = video.objects.all().get(pk=5)
    return render(request, 'impressum.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit})

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
    if lenbw!=0:
        anmtext = bewertung.objects.get(id=lenbw).anm
    else:
        anmtext =""
    if lenbw!=0:
        avgbw1 = round(sumbw1 / i, 1)
        avgbw2 = round(sumbw2 / i, 1)
        avgbw3 = round(sumbw3 / i, 1)
    else:
        avgbw1 = 0
        avgbw2 = 0
        avgbw3 = 0
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

