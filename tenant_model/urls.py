from django.urls import path

from .views import CreateTenantAPIView


urlpatterns = [
    path("createTenant", CreateTenantAPIView.as_view(), name="create-tenant")
]
