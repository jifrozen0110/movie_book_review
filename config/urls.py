from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("users", include("users.urls", namespace="users")),
    path("books", include("books.urls", namespace="books")),
    path("genres", include("categories.urls", namespace="genres")),
    path("movies", include("movies.urls", namespace="movies")),
    path("people", include("people.urls", namespace="people")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)