from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from .serializers import MisiSerializer
from .models import Misi

class CreateMisi(CreateAPIView):
    serializer_class = MisiSerializer
    queryset = Misi.objects.all()

class ListMisi(ListAPIView):
    queryset = Misi.objects.all()
    serializer_class = MisiSerializer

class DeleteMisi(DestroyAPIView):
    queryset = Misi.objects.all()
    serializer_class = MisiSerializer

