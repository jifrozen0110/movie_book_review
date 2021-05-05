from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.MoviesList.as_view(), name="movies"),
    path("<int:pk>", views.MovieDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.MovieUpdateView.as_view(), name="update"),
    path("create/", views.MovieCreateView.as_view(), name="create"),
]
