from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import translation
from .models import bewertungneu
from .models import bewertung
from .models import video
from .forms import aqbw
from .forms import bewertungn
import logging

logger = logging.getLogger(__name__)
zs = False

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
    lang = translation.get_language_from_request(request)
    return render(request, 'home.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit, 'lang':lang})

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
    lang = translation.get_language_from_request(request)
    return render(request, 'projects.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit, 'lang':lang})

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
    lang = translation.get_language_from_request(request)
    return render(request, 'werdegang.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit, 'lang':lang})

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
    lang = translation.get_language_from_request(request)
    return render(request, 'schule.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit, 'lang':lang})

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
    lang = translation.get_language_from_request(request)
    return render(request, 'hobbies.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit, 'lang':lang})

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
    lang = translation.get_language_from_request(request)
    return render(request, 'anschreiben.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit, 'lang':lang})

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
    lang = translation.get_language_from_request(request)
    return render(request, 'ziele.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit, 'zs':True, 'lang':lang})

def bewertungns(request):
    bewertungns1 = bewertungneu.objects.all()
    i = 0
    sumBw1,sumBw2 = 0,0
    sumBw3 = 0
    sumBw4, sumBw5, sumBw6, sumBw7,sumBw8, sumBw9, sumBw10, sumBw11 = 0,0,0,0,0,0,0,0
    lenbw = len(bewertungns1)
    if lenbw!=0:
        for bewertungen in bewertungns1:
            sumBw1  = bewertungen.bw1Formulierung
            sumBw2  += bewertungen.bw1Css
            sumBw3  += bewertungen.bw1Aufbau
            sumBw4  += bewertungen.bw2Fancy
            sumBw5  += bewertungen.bw2Projects
            sumBw6  += bewertungen.bw3Dtl
            sumBw7  += bewertungen.bw3Inhalt
            sumBw8  += bewertungen.bw4Bewe
            sumBw9  += bewertungen.bw5Start
            sumBw10 += bewertungen.bw5Proj
            sumBw11 += bewertungen.bw5Farbe
            i += 1
        obj = bewertungneu.objects.get(id=lenbw)
        anmtext1 = obj.bw1Aenderung
        anmtext2 = obj.bw2Aenderung
        anmtext3 = obj.bw3Aenderung
        anmtext4 = obj.bw4Aenderung
        anmtext5 = obj.bw5Aenderung
        avgBw1  = round(sumBw1 / i,1)
        avgBw2  = round(sumBw2 / i,1)
        avgBw3  = round(sumBw3 / i,1)
        avgBw4  = round(sumBw4 / i,1)
        avgBw5  = round(sumBw5 / i,1)
        avgBw6  = round(sumBw6 / i,1)
        avgBw7  = round(sumBw7 / i,1)
        avgBw8  = round(sumBw8 / i,1)
        avgBw9  = round(sumBw9 / i,1)
        avgBw10 = round(sumBw10 / i,1)
        avgBw11 = round(sumBw11 / i,1)
    else:
        anmtext1,anmtext2,anmtext3,anmtext4,anmtext5 = "Bisher kein vorheriger Text vorhanden!","Bisher kein vorheriger Text vorhanden!","Bisher kein vorheriger Text vorhanden!","Bisher kein vorheriger Text vorhanden!","Bisher kein vorheriger Text vorhanden!"
        avgBw1,avgBw2,avgBw3,avgBw4,avgBw5,avgBw6,avgBw7,avgBw8,avgBw9,avgBw10,avgBw11=0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.
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
    if request.method == 'POST':
        sendBw1 = int(request.POST['bw1Formulierung'])
        sendBw2 = int(request.POST['bw1Css'])    
        sendBw3 = int(request.POST['bw1Aufbau'])    
        sendBw4 = int(request.POST['bw2Fancy'])    
        sendBw5 = int(request.POST['bw2Projects'])    
        sendBw6 = int(request.POST['bw3Dtl'])    
        sendBw7 = int(request.POST['bw3Inhalt'])    
        sendBw8 = int(request.POST['bw4Bewe'])    
        sendBw9 = int(request.POST['bw5Start'])    
        sendBw10 = int(request.POST['bw5Proj'])    
        sendBw11 = int(request.POST['bw5Farbe'])
        sendanm1 = request.POST['bw1Aenderung']
        sendanm2 = request.POST['bw2Aenderung']
        sendanm3 = request.POST['bw3Aenderung']
        sendanm4 = request.POST['bw4Aenderung']
        sendanm5 = request.POST['bw5Aenderung']
        bewertungneu.objects.create(bw1Formulierung=sendBw1, bw1Css=sendBw2, bw1Aufbau=sendBw3, bw1Aenderung=sendanm1, bw2Fancy=sendBw4, bw2Projects=sendBw5, bw2Aenderung=sendanm2, bw3Dtl=sendBw6, bw3Inhalt=sendBw7, bw3Aenderung=sendanm3, bw4Bewe=sendBw8, bw4Aenderung=sendanm4, bw5Start=sendBw9,  bw5Proj=sendBw10, bw5Farbe=sendBw11,bw5Aenderung=sendanm5)
    form = bewertungn()
    return render(request, 'bewertung.html', {'color':color, 'color2':color2, 'colorbw':colorbw, 'avg1':avgBw1, 'avg2':avgBw2, 'avg3':avgBw3, 'avg4':avgBw4, 'avg5':avgBw5, 'avg6':avgBw6, 'avg7':avgBw7, 'avg8':avgBw8, 'avg9':avgBw9, 'avg10':avgBw10, 'avg11':avgBw11, 't1':anmtext1, 't2':anmtext2, 't3':anmtext3, 't4':anmtext4, 't5':anmtext5, 'form':form, 'lenbw':lenbw})

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
    lang = translation.get_language_from_request(request)    
    return render(request, 'videos.html', {'color':color, 'color2':color2, 'colorbw':colorbw, 'videos': videodb, 'rubix':rubix, 'maxit':maxit, 'lang':lang})

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
    lang = translation.get_language_from_request(request)
    return render(request, 'impressum.html', {'name':'Jan', 'color':color, 'color2':color2, 'colorbw':colorbw, 'rubix':rubix, 'maxit':maxit, 'lang':lang})

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
        bewertung.objects.all().create(bw1=sendbw1, bw2=sendbw2, bw3=sendbw3, anm=sendanm)
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

