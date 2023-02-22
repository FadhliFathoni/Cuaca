from django.db import models

def uploadTo(instance, filename):
    return 'static/images/{filename}'.format(filename=filename)

class Tema(models.Model):
    tema = models.CharField(max_length=24)
    primary1 = models.CharField(max_length=20)
    primary2 = models.CharField(max_length=20)
    accent1 = models.CharField(max_length=20)
    poin = models.CharField(max_length=24)
    mainPicture = models.ImageField(upload_to=uploadTo, blank=True, null=True)
    cover = models.ImageField(upload_to=uploadTo, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.tema)

class PenukaranTema(models.Model):
    id_tema = models.IntegerField()
    tema = models.CharField(max_length=24)
    id_user = models.IntegerField()
    user = models.CharField(max_length=150)
    status = models.CharField(max_length=24)

class UsedTema(models.Model):
    id_tema = models.IntegerField()
    tema = models.CharField(max_length=24)
    id_user = models.IntegerField()
    user = models.CharField(max_length=150)
    status = models.CharField(max_length=24)
    primary1 = models.CharField(max_length=20)
    primary2 = models.CharField(max_length=20)
    accent1 = models.CharField(max_length=20)
    mainPicture = models.ImageField(null = True)
    cover = models.ImageField(null = True)

    def __str__(self):
        return "{} {}".format(self.user,self.tema)