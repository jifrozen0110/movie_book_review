from django.db import models
from core import models as core_models


class Book(core_models.TimeStampedModel):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    cover_image = models.ImageField(null=True, blank=True)
    rating = models.IntegerField()
    category = models.ForeignKey("categories.Category", related_name="books", on_delete=models.CASCADE)
    writer = models.ForeignKey("people.Person", related_name="books", on_delete=models.CASCADE)
