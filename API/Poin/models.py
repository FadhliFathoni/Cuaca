from django.db import models

class Poin(models.Model):
    id_user = models.IntegerField()
    email = models.EmailField(max_length=50,unique=True)
    user = models.CharField(max_length=50)
    poin = models.IntegerField()