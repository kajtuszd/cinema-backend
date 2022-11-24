from rest_framework import permissions


class IsModerator(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.user.is_moderator:
            return True
        return False
