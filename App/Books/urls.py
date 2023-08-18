from django.urls import path
from .views import all_books, AuthorViews

urlpatterns = [
    path("v1/books/", all_books, name="all_books"),
    # path("v1/users/<str:user_id>/books/", add_book, name="new_book"),
    path("v1/users/", AuthorViews.as_view(), name="Authors"),
]
