from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import ListAPIView
from API.Misi.models import Misi
from API.Poin.models import Poin
from .models import Penukaran
from .serializers import SerializersPenukaran
from Account.models import User
import jwt

class ListPenukaran(ListAPIView):
    queryset = Penukaran.objects.all()
    serializer_class = SerializersPenukaran

@api_view(["GET","POST"])
def TukarMisi(request, id):
    misi = Misi.objects.get(id = id)
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
    poin = Poin.objects.get(id_user = str(user.id)).poin
    poinUser = Poin.objects.filter(id_user = str(user.id))
    if request.method == "POST":
        if poin >= misi.poin:
            poin = poin - misi.poin
            poinUser.update(
                poin = poin
            )
            Penukaran.objects.create(
                id_user = user.id,
                nama = user.name,
                id_misi = misi.id,
                misi = misi.judul
            )
            return Response("Success")
        else:
            return Response("Point Kurang")
    return Response("Exchange your point")