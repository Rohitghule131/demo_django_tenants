from django.db import models


class DummyModel(models.Model):
    """
    Class for create Dummy model.
    """
    name = models.CharField(max_length=100)