from rest_framework import serializers
from .models import Poin

class getPoin(serializers.ModelSerializer):
    class Meta:
        model = Poin
        fields = ["poin"]