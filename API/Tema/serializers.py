from rest_framework import serializers
from .models import Tema, PenukaranTema

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = "__all__"

class PenukaranTemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenukaranTema
        fields = "__all__"