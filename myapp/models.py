from django.db import models


class DummyModel(models.Model):
    """
    Class for create Dummy model.
    """
    name = models.CharField(max_length=100)


class DummyModel2(models.Model):
    name = models.CharField(max_length=100)


class DummyModel3(models.Model):
    name = models.CharField(max_length=100)
