from rest_framework import serializers
from .models import Tema, TemaUser

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = "__all__"

class UsedTemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemaUser
        fields = "__all__"

class TemaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemaUser
        fields = ["id_tema","tema","icon","status","poin"]