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
