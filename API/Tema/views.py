from Account.models import User
from API.Poin.models import Poin
from .models import Tema, TemaUser
from .serializers import TemaSerializer, UsedTemaSerializer, TemaUserSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
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
@api_view(["GET"])
def ListTema(request):
    user = getUser(request)
    queryset = TemaUser.objects.filter(id_user = user.id)
    serializer = TemaUserSerializer(queryset, many = True)
    return Response(serializer.data)

class List(ListAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

class CreateTema(CreateAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

@api_view(["GET","POST"])
def BeliTema(request, id_tema):
    user = getUser(request)
    poin = Poin.objects.get(id_user = user.id).poin
    tema = Tema.objects.get(id = id_tema)
    if request.method == "POST":
        if poin >= int(tema.poin):
            TemaUser.objects.filter(id_tema = id_tema, id_user = user.id).update(
                purchased = True,
                status = "Purchased"
            )
            Poin.objects.filter(id_user = user.id).update(
                poin = poin - int(tema.poin)
            )
            return Response("Success")
        else:
            return Response("Poin kurang")
    return Response()
    
@api_view(["GET"])
def ListPurchased(request):
    try:
        user = getUser(request)
        queryset = TemaUser.objects.filter(status = "Purchased",id_user = user.id)
        serializer = TemaUserSerializer(queryset, many = True)
        return Response(serializer.data)
    except:
        return Response("User didn't have any theme")

@api_view(["GET"])
def TemaAktif(request):
    user = getUser(request)
    yourTema = TemaUser.objects.get(id_user = user.id, status = "Active")
    serializer = UsedTemaSerializer(yourTema, many = False)
    return Response(serializer.data)

@api_view(["GET","POST"])
def UbahTema(request, id_tema):
    user = getUser(request)
    if request.method == "POST":
        try:
            if TemaUser.objects.get(id_user = user.id, id_tema = id_tema ,status = "Purchased"):
                TemaUser.objects.filter(id_user = user.id,status = "Active").update(status = "Purchased")
                TemaUser.objects.filter(id_user = user.id,id_tema = id_tema).update(status = "Active")
                return Response("Berhasil Diubah")
        except:
            return Response("Tema belum dibeli")
    return Response()