from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
  list_display=(
    "title",
    "writer",
    "year",
    "category",
    "cover_image",
    "rating",

  )

  list_fileter=(
    "rating",
    "category",
  )