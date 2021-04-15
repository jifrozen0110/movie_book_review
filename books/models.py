from django.db import models
from core import models as core_models
"""
Here are the models you have to create:
- Book:
  title
  year
  category (ForeignKey => categories.Category)
  cover_image
  rating
  writer (ForeignKey => people.Person)
"""
class Book(core_models.TimeStampedModel):
  title=models.CharField(max_length=100)
  year=models.CharField(max_length=10)
  cover_image=models.ImageField(null=True,blank=True)
  rating=models.IntegerField()
  category=models.ForeignKey("categories.Category",related_name="books",on_delete=models.CASCADE)
  writer=models.ForeignKey("people.Person",related_name="books",on_delete=models.CASCADE)
  def __str__(self):
    return self.title