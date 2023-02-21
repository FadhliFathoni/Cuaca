from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListMisi.as_view()),
    path('list/',views.ListTerima.as_view()),
    path('create/',views.CreateMisi.as_view()),
    path('<int:misi_id>/terima',views.GetMisi),
    path('<pk>/delete',views.DeleteMisi.as_view()),
]
