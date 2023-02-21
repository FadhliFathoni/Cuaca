from rest_framework import serializers
from .models import Misi, TerimaMisi

class MisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Misi
        fields = "__all__"

class TerimaMisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerimaMisi
        fields = "__all__"