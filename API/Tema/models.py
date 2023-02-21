from django.db import models

class Tema(models.Model):
    main = models.CharField(max_length=20)
    secondary = models.CharField(max_length=20)
    accent = models.CharField(max_length=20)