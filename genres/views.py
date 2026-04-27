from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializers import GenreSerializer
from genres.permissions import GenrePermission


# Criando as views para CRUD
class GenreListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenrePermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GenrePermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer




