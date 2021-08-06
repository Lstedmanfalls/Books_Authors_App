from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("books/create_book", views.create_book),
    path("books/<int:book_id>", views.book_profile),
    path("books/<int:book_id>/add_author", views.add_author),
    path("authors", views.author),
    path("authors/create_author", views.create_author),
    path("authors/<int:author_id>", views.author_profile),
    path("authors/<int:author_id>/add_book", views.add_book),
]