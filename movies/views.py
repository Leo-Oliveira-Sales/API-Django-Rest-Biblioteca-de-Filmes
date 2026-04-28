from django.db.models import Count, Avg
from rest_framework import generics, views, response
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieModelSerializer
from reviews.models import Review


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)  # autenticação
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = Movie.objects.count()  # ou self.queryset.count()
        movies_by_genres = Movie.objects.values('genre__name').annotate(total=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg=Avg('stars'))['avg']

        return response.Response({
            'total_movies': total_movies,
            'movies_by_genres': movies_by_genres,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0,  # Evita erro se nao houver avaliação
        })


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
