from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,CreateView
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
class MovieDetailView(DetailView):
  model=Movie

class MovieUpdateView(UpdateView):
    model = Movie
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
    )

class MovieCreateView(CreateView):
  model=Movie
  fields=(
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
  )
