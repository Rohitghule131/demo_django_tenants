from rest_framework import serializers
from .models import (
    TenantModel,
    DomainModel
)


class CreateTenantSerializer(serializers.ModelSerializer):
    """
    Class for create tenant serializer.
    """
    domain = serializers.CharField(required=True, write_only=True)
    domain_name = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = TenantModel
        fields = ("id", "name", "schema_name", "paid_until", "on_trial", "domain", "domain_name")


class DomainSerializer(serializers.ModelSerializer):
    """
    Class for create tenant serializer.
    """

    class Meta:
        model = DomainModel
        fields = ("id", "domain", "domain_name", "tenant", "is_primary")
