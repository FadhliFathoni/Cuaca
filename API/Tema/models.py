from django.db import models

def uploadTo(instance, filename):
    return 'static/images/{filename}'.format(filename=filename)

class Tema(models.Model):
    tema = models.CharField(max_length=24)
    primary1 = models.CharField(max_length=20)
    primary2 = models.CharField(max_length=20)
    accent1 = models.CharField(max_length=20)
    poin = models.IntegerField()
    cover = models.ImageField(upload_to=uploadTo, blank=True, null=True)

class PenukaranTema(models.Model):
    id_tema = models.IntegerField()
    tema = models.CharField(max_length=24)
    id_user = models.IntegerField()
    user = models.CharField(max_length=150)
    waktu = models.IntegerField()
    poin = models.IntegerField()
    status = models.CharField(max_length=24)