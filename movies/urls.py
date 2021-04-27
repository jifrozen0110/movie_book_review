from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.MoviesList.as_view(), name="movies"),
    path("<int:pk>", views.MovieDetailView.as_view(), name="movie_detail"),
    path("<int:pk>/edit/", views.MovieUpdateView.as_view(), name="movie_update"),
    path("create/", views.MovieCreateView.as_view(), name="movie_create"),
]
