from API.Tema.models import Tema
from API.Tema.serializers import TemaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def tes(request):
    tema = Tema.objects.all()
    for x in tema:
        print(x)
    serializer = TemaSerializer(tema, many=True)
    return Response(serializer.data)