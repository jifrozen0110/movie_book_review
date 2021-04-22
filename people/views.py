from django.shortcuts import render


def all_people(request):
    return render(request, "people.html")
