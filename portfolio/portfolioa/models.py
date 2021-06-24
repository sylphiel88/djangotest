from django.db import models

# Create your models here.


class bewertung(models.Model):
    bw1 = models.IntegerField()
    bw2 = models.IntegerField()
    bw3 = models.IntegerField()
    anm = models.TextField()

class video(models.Model):
    title = models.CharField(max_length=100)
    videofile = models.FileField(upload_to='videos')
    previewimg = models.FileField(upload_to='pics')

class bewertungneu(models.Model):
     bw1Formulierung = models.IntegerField()
     bw1Css = models.IntegerField()
     bw1Aufbau = models.IntegerField()
     bw1Aenderung = models.TextField()
     bw2Fancy = models.IntegerField()
     bw2Projects = models.IntegerField()
     bw2Aenderung = models.TextField()
     bw3Dtl = models.IntegerField()
     bw3Inhalt = models.IntegerField()
     bw3Aenderung = models.TextField()
     bw4Bewe = models.IntegerField()
     bw4Aenderung = models.TextField()
     bw5Start = models.IntegerField()
     bw5Proj = models.IntegerField()
     bw5Farbe = models.IntegerField()
     bw5Aenderung = models.TextField()



    
