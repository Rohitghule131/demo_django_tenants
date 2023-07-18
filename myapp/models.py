from django.db import models


class Book(models.Model):
    """
    Class to create model for books.
    """
    name = models.CharField(max_length=30, null=False, blank=False)
    author = models.CharField(max_length=30, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
