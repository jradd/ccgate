from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object `modify` permissions.
    """

    def has_object_permission(self, request, view, obj):
        # Allow read only permissions to non authenticated users.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow read/write to the object owner.
        return obj.author == request.user