from django.db import models

class Misi(models.Model):
    judul = models.CharField(max_length=120)
    gambar = models.CharField(max_length=120)
    poin = models.IntegerField()
    waktu = models.IntegerField()

    def __str__(self):
        return "{}".format(self.judul)

class TerimaMisi(models.Model):
    id_misi = models.IntegerField(null=True)
    misi = models.CharField(max_length=120,null=True)
    id_user = models.IntegerField(null=True)
    user = models.CharField(max_length=150,null=True)
    waktu = models.IntegerField()
    remaining = models.FloatField(null=True)
    end_time = models.FloatField(null=True)
    poin = models.IntegerField()
    status = models.CharField(max_length=24)

    def __str__(self):
        return "{} {}".format(self.user, self.misi)
