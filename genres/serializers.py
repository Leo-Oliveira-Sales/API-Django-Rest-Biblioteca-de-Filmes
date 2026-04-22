from rest_framework import serializers
from genres.models import Genre


# Criando o serializer para ser usado nas views
class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = "__all__"