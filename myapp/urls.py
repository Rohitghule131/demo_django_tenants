from django.urls import path

from .views import (
    AddBookAPIView,
    ListBooksAPIView,
    UpdateBooksAPIView
)


urlpatterns = [
    path("addBook", AddBookAPIView.as_view(), name="add-book"),
    path("listBooks", ListBooksAPIView.as_view(), name="list-books"),
    path("updateBook/<int:pk>", UpdateBooksAPIView.as_view(), name="update-book"),
]