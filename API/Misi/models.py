from django.db import models

def uploadTo(instance, filename):
    return 'static/images/{filename}'.format(filename=filename)

class Misi(models.Model):
    judul = models.CharField(max_length=120)
    gambar = models.ImageField(upload_to=uploadTo, blank=True, null=True)
    poin = models.IntegerField()
    waktu = models.IntegerField()

class TerimaMisi(models.Model):
    id_misi = models.IntegerField()
    misi = models.CharField(max_length=120)
    id_user = models.IntegerField()
    user = models.CharField(max_length=150)
    waktu = models.IntegerField()
    poin = models.IntegerField()
    status = models.CharField(max_length=24)
