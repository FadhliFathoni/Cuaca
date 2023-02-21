from rest_framework import serializers
from .models import Misi

class MisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Misi
        fields = "__all__"