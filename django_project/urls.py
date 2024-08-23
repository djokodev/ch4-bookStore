from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # path("accounts/", include("django.contrib.auth.urls")), #use the auth provide by django
    # path("accounts/", include("accounts.urls")), 

    path("accounts/", include("allauth.urls")), # use auth django-allauth
    path('', include("pages.urls")),
    path("books/", include("books.urls")), 

]
