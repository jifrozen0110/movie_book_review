from django.db import models
from core import models as core_models

class Review(core_models.TimeStampedModel):
    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE,related_name="reviews")
    text = models.TextField()
    rating = models.IntegerField()
    movie = models.ForeignKey("movies.Movie", related_name="reviews", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by
