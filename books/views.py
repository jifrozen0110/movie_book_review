from django.shortcuts import render


def all_books(request):
    return render(request, "books.html")
