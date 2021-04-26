from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.MoviesList.as_view(), name="movies")
]
