from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Tema
from .serializers import TemaSerializer

class ListTema(ListAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

class CreateTema(CreateAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer