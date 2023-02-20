from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from API.Poin.models import Poin
from .serializers import getUser
from API.Poin.serializers import getPoin
from rest_framework.exceptions import AuthenticationFailed
import jwt

# Create your views here.

@api_view(["GET"])
def getUser(request):
    token = request.headers.get('jwt')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    user = User.objects.get(id=payload['id'])
    poin = Poin.objects.get(id_user = str(user.id)).poin
    context = {
        "nama":user.name,
        "email":user.email,
        "password":user.password,
        "gambar":user.foto,
        "poin":poin,
    }
    return Response(context)