from django.urls import path
from . import views

urlpatterns = [
    path("",views.ListTema.as_view()),
    path("create/",views.CreateTema.as_view()),
]
