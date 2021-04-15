from django.db import models
from core import models as core_models


"""
Here are the models you have to create:
- Movie:
  title
  year
  cover_image
  rating
  category (ManyToMany => categories.Category)
  director (ForeignKey => people.Person)
  cast (ManyToMany => people.Person)
"""

class Movie(core_models.TimeStampedModel):
  title=models.CharField(max_length=100)
  year=models.CharField(max_length=10)
  cover_image=models.ImageField(null=True,blank=True)
  rating=models.IntegerField()
  category=models.ManyToManyField("categories.Category",related_name="movies",blank=True)
  director=models.ForeignKey("people.Person",related_name="movies",on_delete=models.CASCADE)
  def __str__(self):
    return self.title


