from django.contrib import admin
from django.urls import path
from . import views

app_name = "app_homework10"

urlpatterns = [
    path("", views.quotes, name='quotes'),
    path("quotes/", views.quotes, name='quotes'),
    path("authors/", views.authors, name='authors'),
    path("authors/<int:author_id>", views.author_card, name='author_card'),
    path("author_add", views.author_add, name='author_add'),
    path("quote_add", views.quote_add, name='quote_add'),
]