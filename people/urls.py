from django.urls import path
from . import views

app_name = "people"

urlpatterns = [
    path("", views.PeopleView.as_view(), name="people")
]
