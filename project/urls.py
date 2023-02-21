from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Account.urls')),
    path('poin/',include('API.Poin.urls')),
    path('misi/',include('API.Misi.urls')),
    path('tukar/',include('API.Penukaran.urls')),
]
