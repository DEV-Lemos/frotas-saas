# helpers de permissão por empresa

from rest_framework.permissions import BasePermission


class IsTenantUser(BasePermission):
    """
    Custom permission to only allow access to users of the same tenant.
    """

    def has_permission(self, request, view):
        # Check if the user belongs to the tenant
        return request.user.tenant_id == request.tenant_id
