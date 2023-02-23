from rest_framework import serializers
from .models import Tema, UsedTema, TemaUser

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = "__all__"

class UsedTemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsedTema
        fields = "__all__"

class TemaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemaUser
        fields = "__all__"