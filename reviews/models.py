from django.db import models
from core import models as core_models


"""
Here are the models you have to create:
- Review
  created_by (ForeignKey => users.User)
  text
  movie (ForeignKey => movies.Movie, null,blank)
  book (ForeignKey => movies.Movie, null,blank)
  rating
"""
class Review(core_models.TimeStampedModel):
  created_by=models.ForeignKey("users.User",on_delete=models.CASCADE)
  text=models.TextField()
  rating=models.IntegerField()
  movie=models.ForeignKey("movies.Movie",null=True,blank=True,on_delete=models.CASCADE)
  book=models.ForeignKey("books.Book",null=True,blank=True,on_delete=models.CASCADE)


  def __str__(self):
    return self.created_by
