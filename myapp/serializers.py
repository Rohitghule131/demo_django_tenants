from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Class to craete book serializer.
    """
    class Meta:
        model = Book
        fields = ("id", "name", "author", "price", "created_at", "updated_at")
