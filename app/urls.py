from django.contrib import admin
from django.urls import path
from genres.views import GenreListCreateView, GenreRetrieveUpdateDestroyView


# Criando as urls para as views de CRUD dos gêneros
urlpatterns = [
    path("admin/", admin.site.urls),

    path("genres/", GenreListCreateView.as_view(), name="genre_create_list"),
    path("genres/<int:pk>/", GenreRetrieveUpdateDestroyView.as_view(), name="genre_detail_view"),
]
