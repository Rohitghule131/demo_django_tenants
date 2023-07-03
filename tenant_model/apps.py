from django.apps import AppConfig


class TenantModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tenant_model'
