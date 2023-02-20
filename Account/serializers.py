from rest_framework import serializers
from .models import User

class getUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name","email","phone","photo"]