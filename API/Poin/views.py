from rest_framework.generics import ListAPIView
from .models import Poin
from .serializers import getPoin

class getPoin(ListAPIView):
    queryset = Poin.objects.all()
    serializer_class = getPoin