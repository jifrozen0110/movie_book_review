from django.db import models
from core import models as core_models
"""
Here are the models you have to create:
- FavList
  created_by (OneToOne => users.User)
  books (ManyToMany => books.Book)
  movies (ManyToMany => movies.Movie)
"""
class Fav(core_models.TimeStampedModel):
  created_by=models.OneToOneField("users.User",on_delete=models.CASCADE)
  books=models.ManyToManyField("books.Book",related_name="favs",blank=True)
  movies=models.ManyToManyField("movies.Movie",related_name="favs",blank=True)