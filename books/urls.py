from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.BooksView.as_view(), name="books"),
    path("<int:pk>/", views.BookDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.BookUpdateView.as_view(), name="update"),
    path("create/", views.BookCreateView.as_view(), name="create"),
]
