from django.urls import path
from . import views

urlpatterns = [
    path("",views.ListTema),
    path("list/",views.List.as_view()),
    path("aktif",views.TemaAktif),
    path("purchased/",views.ListPurchased),
    path("<int:id_tema>/beli",views.BeliTema),
    path("<int:id_tema>/ubah",views.UbahTema),

    path("create/",views.CreateTema.as_view()),
]
