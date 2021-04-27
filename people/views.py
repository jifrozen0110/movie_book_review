from django.views.generic import ListView, DetailView, UpdateView, CreateView
from people.models import Person


class PeopleView(ListView):
    model = Person
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "people"
    template_name = "people/people_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All People"
        return context


class PeopleDetailView(DetailView):
    model = Person
    template_name = "people/people_detail.html"


class PeopleUpdateView(UpdateView):
    model = Person
    fields = (
        "name",
        "photo",
        "kind",
    )
    template_name = "people/people_form.html"


class PeopleCreateView(CreateView):
    model = Person
    fields = (
        "name",
        "photo",
        "kind",
    )
    template_name = "people/people_form.html"
