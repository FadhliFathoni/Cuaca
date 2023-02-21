from django.db import models

class Penukaran(models.Model):
    id_user = models.IntegerField()
    nama = models.CharField(max_length=50)
    id_misi = models.IntegerField()
    misi = models.CharField(max_length=120)