from django.shortcuts import render
from django.views.generic import ListView
from movies.models import Movie


class MoviesList(ListView):
    model = Movie
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All Movies"
        return context
