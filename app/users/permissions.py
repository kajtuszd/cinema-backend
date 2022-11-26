from rest_framework import permissions


class IsModerator(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.user.is_moderator:
            return True
        return False


class IsModeratorOrOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.user.is_moderator and request.method in permissions.SAFE_METHODS:
            return True
        if obj == request.user:
            return True
        return False
