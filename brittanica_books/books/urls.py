from django.urls import path
from .views import UserView, BooksView

urlpatterns = [
    path("users/",UserView.as_view(),name="users"),
    path("users/<int:pk>",UserView.as_view(),name="user_update"),
    path("books/",BooksView.as_view(),name="books"),
    path("books/<int:pk>",BooksView.as_view(),name="books")

]