from django.db import models
from django_tenants.models import (
                                    TenantMixin,
                                    DomainMixin
                                  )


class TenantModel(TenantMixin):
    """
    Class for create client model using TenantMixin.
    """
    name = models.CharField(max_length=200, null=False, blank=False)
    paid_until = models.DateField(null=True, blank=False)
    on_trial = models.BooleanField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    auto_create_schema = True


class DomainModel(DomainMixin):
    """
    Class for create domain for the tenant.
    """
    domain_name = models.CharField(max_length=50, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

