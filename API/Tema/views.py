from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Tema, PenukaranTema
from Account.models import User
from .serializers import TemaSerializer, PenukaranTemaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
import jwt

def getUser(request):
    token = ""
    jwt_cookie = request.headers.get('Cookie')
    if jwt_cookie:
        cookies = {c.split('=')[0]: c.split('=')[1] for c in jwt_cookie.split('; ')}
        token = cookies.get('jwt')
    else:
        pass
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    user = User.objects.get(id=payload['id'])
    return user

class ListTema(ListAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

class CreateTema(CreateAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

@api_view(["POST"])
def BeliTema(request, id_tema):
    user = getUser(request)
    tema = Tema.objects.get(id = id_tema)
    PenukaranTema.objects.create(
        id_tema = id_tema,
        tema = tema.tema,
        id_user = user.id,
        user = user.name,
        status = "Purchased"
    )

@api_view(["GET"])
def ListPurchased(request):
    user = getUser(request)
    queryset = PenukaranTema.objects.filter(status = "Purchased",id_user = user.id)
    serializer = PenukaranTemaSerializer(queryset, many = True)
    return Response(serializer.data)