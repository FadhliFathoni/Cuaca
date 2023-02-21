from rest_framework import serializers
from .models import Penukaran

class SerializersPenukaran(serializers.ModelSerializer):
    class Meta:
        model = Penukaran
        fields = "__all__"