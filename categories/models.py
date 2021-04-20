from django.db import models
from core import models as core_models


class Category(core_models.TimeStampedModel):
    KIND_MOVIE = "movie"
    KIND_BOOK = "book"
    KIND_BOTH = "both"

    KIND_CHOICES = (
        (KIND_MOVIE, "movie"),
        (KIND_BOOK, "book"),
        (KIND_BOTH, "both"),
    )

    name = models.CharField(max_length=100)
    kind = models.CharField(choices=KIND_CHOICES, max_length=10, default=KIND_BOTH)

    def __str__(self):
        return self.name

