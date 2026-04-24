from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg


class MovieModelSerializer(serializers.ModelSerializer):
    # Campos calculados
    rate = serializers.SerializerMethodField() # Por padrão é read_only=True. Somente leitura!

    class Meta:
        model = Movie
        fields = '__all__'
    
    # Campos calculados
    # Pode ser feito em views. É mais performático e profissional | consultar views.py
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg("stars"))['stars__avg'] # or 0
        if rate:
            return round(rate, 1)

    # Validações
    def validate_release_date(self, value):
        if value.year < 1990: 
            raise serializers.ValidationError("O ano de lançamento deve ser maior ou igual a 1990.")
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("O resumo não deve ser maior do que 200 caracteres.")
        return value
    
