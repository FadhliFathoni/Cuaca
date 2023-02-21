from django.db import models

class Tema(models.Model):
    primary1 = models.CharField(max_length=20)
    primary2 = models.CharField(max_length=20)
    accent1 = models.CharField(max_length=20)
    poin = models.IntegerField()
    cover = models.ImageField()