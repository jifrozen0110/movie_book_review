from django.db import models
from core import models as core_models


class Fav(core_models.TimeStampedModel):
    created_by = models.OneToOneField("users.User", on_delete=models.CASCADE)
    books = models.ManyToManyField("books.Book", related_name="favs")
    movies = models.ManyToManyField("movies.Movie", related_name="favs")

    def __str__(self):
        return f"{self.created_by}'s Fav List"
