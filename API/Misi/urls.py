from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListTerima),
    path('<int:misi_id>/terima',views.GetMisi),
    path('<pk>/cancel',views.CancelMisi.as_view()),
    path('<int:id>/complete',views.MissionComplete),
    
    path('list/',views.ListMisi.as_view()),
    path('create/',views.CreateMisi.as_view()),
    path('<pk>/delete',views.DeleteMisi.as_view()),
]
