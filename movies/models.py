from django.db import models
from core import models as core_models


class Movie(core_models.TimeStampedModel):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    cover_image = models.ImageField(null=True,blank=True)
    rating = models.IntegerField()
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE, related_name="movies")
    director = models.ForeignKey("people.Person", related_name="movies", on_delete=models.CASCADE)
    cast = models.ManyToManyField("people.Person")

