from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
  list_display=(
    "title",
    "year",
    "rating",

  )

  list_fileter=(
    "rating",
    "category",
  )