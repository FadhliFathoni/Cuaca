from django.urls import path
from . import views

urlpatterns = [
    path('user/',views.getUser),
    path('login/',views.LoginView.as_view()),
    path('logout/',views.LogoutView.as_view()),
    path('register/',views.RegisterView.as_view()),
]
