from django.contrib import admin
from django.urls import path, include
from .views import register, log_in


urlpatterns = [
    path("register/", register, name="register"),
    path('', include("django.contrib.auth.urls")),
]
