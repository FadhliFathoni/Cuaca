from django.urls import path
from . import views

urlpatterns = [
    path("",views.ListPenukaran.as_view()),
    path("<int:id>",views.TukarMisi),
]
