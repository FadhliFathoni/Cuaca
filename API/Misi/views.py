from .serializers import MisiSerializer, TerimaMisiSerializer
from .models import Misi, TerimaMisi
from API.Poin.models import Poin
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from Account.models import User
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

class CreateMisi(CreateAPIView):
    serializer_class = MisiSerializer
    queryset = Misi.objects.all()

class ListMisi(ListAPIView):
    queryset = Misi.objects.all()
    serializer_class = MisiSerializer

class DeleteMisi(DestroyAPIView):
    queryset = Misi.objects.all()
    serializer_class = MisiSerializer

@api_view(["GET","POST"])
def GetMisi(request,misi_id):
    user = getUser(request)
    try:
        misi = Misi.objects.get(id = misi_id)
    except:
        return Response("Mission is missing")
    if request.method == "POST":
        TerimaMisi.objects.create(
            id_misi = misi.id,
            misi = misi.judul,
            id_user = user.id,
            user = user.name,
            waktu = misi.waktu,
            poin = misi.poin,
            status = "Pending",
        )
        return Response("Success")
    else:
        return Response("Failed")
    
@api_view(["GET"])
def ListTerima(request):
    user = getUser(request)
    queryset = TerimaMisi.objects.filter(status = "Pending",id_user = user.id)
    serializer = TerimaMisiSerializer(queryset, many=True)
    return Response(serializer.data)

class CancelMisi(DestroyAPIView):
    queryset = TerimaMisi.objects.all()
    serializer_class = TerimaMisiSerializer

@api_view(["GET","POST"])
def MissionComplete(request, id):
    if request.method == "POST":
        try:
            user = getUser(request)
            misi = TerimaMisi.objects.get(id = id)
            poinUser = Poin.objects.get(id_user = user.id).poin
            Poin.objects.filter(id_user = user.id).update(
                poin = poinUser + misi.poin
            )
            TerimaMisi.objects.filter(id = id).delete()
            return Response("Success")
        except:
            return Response("Failed")
    return Response()
