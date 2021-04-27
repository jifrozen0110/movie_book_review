from django.urls import path
from . import views

app_name = "people"

urlpatterns = [
    path("", views.PeopleView.as_view(), name="people"),
    path("<int:pk>", views.PeopleDetailView.as_view(), name="person_detail"),
    path("<int:pk>/edit/", views.PeopleUpdateView.as_view(), name="person_update"),
    path("create/", views.PeopleCreateView.as_view(), name="person_create"),
]
