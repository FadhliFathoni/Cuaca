from django.urls import path
from . import views

urlpatterns = [
    path("",views.getPoin.as_view())
]
