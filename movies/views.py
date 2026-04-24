from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieModelSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

# Campos calculados 
# Pode ser feito em serializers porem aqui é mais performático e profissional | consultar serializers.py

# por em serilaizers.py na class MovieModelSerializer:
# rate = serializers.DecimalField(max_digits=2, decimal_places=1, read_only=True) = leitura e arrendodamento

# from django.db.models import Avg
# from rest_framework.viewsets import ModelViewSet

# class MovieViewSet(ModelViewSet):
#     queryset = Movie.objects.annotate(rate=Avg("reviews__stars"))
#     serializer_class = MovieModelSerializer

# annotate() cria um campo extra rate que vai calcular a media de stars da tabela reviews