from django.views.generic import ListView
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