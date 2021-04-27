from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView,CreateView
from books.models import Book


class BooksView(ListView):
    model = Book
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All Books"
        return context


class BookDetailView(DetailView):
    model = Book


class BookUpdateView(UpdateView):
    model = Book
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "writer",
    )

class BookCreateView(CreateView):
  model=Book
  fields=(
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "writer",
  )
