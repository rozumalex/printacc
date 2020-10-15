from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            return bool(request.user.is_admin)
        except AttributeError:
            return False


class IsDealer(BasePermission):
    def has_permission(self, request, view):
        try:
            return bool(request.user.is_admin)
        except AttributeError:
            return False


class IsAnnonymous(BasePermission):
    def has_permission(self, request, view):
        try:
            return bool(request.user.is_anonymous)
        except AttributeError:
            return False
