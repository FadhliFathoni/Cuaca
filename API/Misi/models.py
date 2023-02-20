from django.db import models

def uploadTo(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Misi(models.Model):
    judul = models.CharField(max_length=120)
    gambar = models.ImageField(upload_to=uploadTo, blank=True, null=True)
    poin = models.IntegerField()
    waktu = models.IntegerField()
    status = models.CharField(max_length=24)