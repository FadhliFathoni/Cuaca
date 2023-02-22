from django.urls import path
from . import views

urlpatterns = [
    path("",views.ListTema.as_view()),
    path("aktif",views.TemaAktif),
    path("purchased/",views.ListPurchased),
    path("<int:id_tema>/beli",views.BeliTema),

    path("create/",views.CreateTema.as_view()),
]
