from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Book
from utilities import messages
from .serializers import BookSerializer
from utilities.utils import ResponseInfo


class AddBookAPIView(CreateAPIView):
    """
    Class to create api for adding book.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = BookSerializer

    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(AddBookAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        """
        Post method to save book details.
        """
        book_serializer = self.get_serializer(data=request.data)
        if book_serializer.is_valid(raise_exception=True):
            book_serializer.save()

            self.response_format["data"] = book_serializer.data
            self.response_format["status_code"] = status.HTTP_201_CREATED
            self.response_format["error"] = None
            self.response_format["message"] = [messages.CREATED.format("Book")]

        return Response(self.response_format)


class ListBooksAPIView(ListAPIView):
    """
    CLass to create api for listing all books
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = BookSerializer

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(ListBooksAPIView).__init__(**kwargs)

    def get_queryset(self):
        return Book.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Get method to get list of books.
        """
        book_serializer = super().list(request, *args, **kwargs)
        self.response_format["satus_code"] = status.HTTP_200_OK
        self.response_format["data"] = book_serializer.data
        self.response_format["error"] = None
        self.response_format["message"] = [messages.SUCCESS]

        return Response(self.response_format)


class UpdateBooksAPIView(UpdateAPIView):
    """
    CLass to create api for an update book.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = BookSerializer

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(UpdateBooksAPIView).__init__(**kwargs)

    def get_queryset(self):
        book_id = self.kwargs.get("pk")
        return Book.objects.get(id=book_id)

    def patch(self, request, *args, **kwargs):
        """
        PATCH method to update the book.
        """
        try:
            book_obj = self.get_queryset()
            book_serializer = self.get_serializer(book_obj, data=request.data, partial=True)

            if book_serializer.is_valid(raise_exception=True):
                book_serializer.save()

                self.response_format["satus_code"] = status.HTTP_200_OK
                self.response_format["data"] = book_serializer.data
                self.response_format["error"] = None
                self.response_format["message"] = [messages.SUCCESS]

        except Book.DoesNotExist:

            self.response_format["satus_code"] = status.HTTP_400_BAD_REQUEST
            self.response_format["data"] = None
            self.response_format["error"] = "Book"
            self.response_format["message"] = [messages.DOES_NOT_EXIST]

        return Response(self.response_format)
