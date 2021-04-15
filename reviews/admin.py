from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "created_by",
        "rating",
        "movie",
        "book",
    )

