from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField() # Campos calculados
    # SerializerMethodField() = Somente leitura / read_only=True. Por padrão!

    class Meta:
        model = Movie
        fields = '__all__'
    
    # Campos calculados
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg("stars"))['stars__avg'] or 0
        return round(rate, 1)

    # Tambem pode ser feito assim: return obj.reviews.aggregate(avg=Avg('stars'))['avg'] or 0


    # Validações
    def validate_release_date(self, value):
        if value.year < 1990: 
            raise serializers.ValidationError("O ano de lançamento deve ser maior ou igual a 1990.")
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("O resumo não deve ser maior do que 200 caracteres.")
        return value
    
