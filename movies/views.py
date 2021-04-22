from django.shortcuts import render

def all_movies(request):
    return render(request,"movies.html")
