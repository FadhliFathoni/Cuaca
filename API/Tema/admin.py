from django.contrib import admin
from .models import Tema, UsedTema, TemaUser

admin.site.register(Tema)
admin.site.register(UsedTema)
admin.site.register(TemaUser)