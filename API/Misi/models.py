from django.db import models

class Misi(models.Model):
    judul = models.CharField(max_length=120)
    gambar = models.CharField(max_length=120)
    poin = models.IntegerField()
    waktu = models.IntegerField()

    def __str__(self):
        return "{}".format(self.judul)

class TerimaMisi(models.Model):
    id_misi = models.IntegerField()
    misi = models.CharField(max_length=120)
    id_user = models.IntegerField()
    user = models.CharField(max_length=150)
    waktu = models.IntegerField()
    poin = models.IntegerField()
    status = models.CharField(max_length=24)
