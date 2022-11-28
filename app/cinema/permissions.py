from rest_framework import permissions


class IsModeratorOrOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.user.is_moderator and request.method in permissions.SAFE_METHODS:
            return True
        if obj.owner == request.user:
            return True
        return False
