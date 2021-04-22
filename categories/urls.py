from django.urls import path
from . import views

app_name = "genres"

urlpatterns = [
    path("", views.all_categories, name="genres")
]
