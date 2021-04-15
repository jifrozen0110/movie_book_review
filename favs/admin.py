from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Fav)
class FavsAdmin(admin.ModelAdmin):
    list_display = (
        "created_by",
    )
