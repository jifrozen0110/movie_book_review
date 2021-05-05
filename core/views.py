from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from movies.models import Movie
from books.models import Book
from people.models import Person
from categories.models import Category


def home(request):

    movies = Movie.objects.all().order_by('pk')[:10]
    books = Book.objects.all().order_by('pk')[:10]
    people = Person.objects.all().order_by('pk')[:10]


    return render(request, "home.html", {
        "movies": movies,
        "books": books,
        "people": people,
        "page_title": "Home"
    })


def search(request):
    return render(request, "search.html", {
        "categories": Category.objects.all()
    })