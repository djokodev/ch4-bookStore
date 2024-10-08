from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),

    # path("accounts/", include("django.contrib.auth.urls")), #use the auth provide by django
    # path("accounts/", include("accounts.urls")), 

    path("accounts/", include("allauth.urls")), # use auth django-allauth
    path('', include("pages.urls")),
    path("books/", include("books.urls")), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
