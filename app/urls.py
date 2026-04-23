from django.contrib import admin
from django.urls import path
from genres.views import GenreListCreateView, GenreRetrieveUpdateDestroyView
from actors.views import ActorListCreateView, ActorRetrieveUpdateDestroyView
from movies.views import MovieListCreateView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewListCreateView, ReviewRetrieveUpdateDestroyView


# Criando as urls para as views de CRUD dos gêneros
urlpatterns = [
    path("admin/", admin.site.urls),

    path("genres/", GenreListCreateView.as_view(), name="genre_create_list"),
    path("genres/<int:pk>/", GenreRetrieveUpdateDestroyView.as_view(), name="genre_detail_view"),

    path("actors/", ActorListCreateView.as_view(), name="actor_create_list"),
    path("actors/<int:pk>/", ActorRetrieveUpdateDestroyView.as_view(), name="actor_detail_view"),

    path("movies/", MovieListCreateView.as_view(), name="movie_create_list"),
    path("movies/<int:pk>/", MovieRetrieveUpdateDestroyView.as_view(), name="movie_detail_view"),

    path("reviews/", ReviewListCreateView.as_view(), name="review_create_list"),
    path("reviews/<int:pk>/", ReviewRetrieveUpdateDestroyView.as_view(), name="review_detail_view"),
]
