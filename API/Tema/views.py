from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Tema
from .serializers import TemaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
import jwt

class ListTema(ListAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

class CreateTema(CreateAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

# @api_view(["POST"])
# def TukarTema(request, id_tema):
    