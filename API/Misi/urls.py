from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListMisi.as_view()),
    path('create/',views.CreateMisi.as_view()),
    path('<pk>/delete',views.DeleteMisi.as_view()),
]
