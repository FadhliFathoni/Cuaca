from django.db import models

def uploadTo(instance, filename):
    return 'static/images/{filename}'.format(filename=filename)

class Tema(models.Model):
    tema = models.CharField(max_length=24)
    primary1 = models.CharField(max_length=20)
    primary2 = models.CharField(max_length=20)
    accent1 = models.CharField(max_length=20)
    accent2 = models.CharField(max_length=20, null=True)
    poin = models.CharField(max_length=24)
    mainPicture = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.tema)

class TemaUser(models.Model):
    id_tema = models.IntegerField()
    tema = models.CharField(max_length=24)
    id_user = models.IntegerField()
    user = models.CharField(max_length=150)
    primary1 = models.CharField(max_length=20)
    primary2 = models.CharField(max_length=20)
    accent1 = models.CharField(max_length=20)
    accent2 = models.CharField(max_length=20,null=True)
    mainPicture = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    purchased = models.BooleanField(null= True)
    status = models.CharField(max_length=24)
    poin = models.CharField(max_length=24, null=True)

    def __str__(self):
        return "{} {} {}".format(self.user, self.tema, self.purchased)