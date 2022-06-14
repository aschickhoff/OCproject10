from rest_framework.permissions import BasePermission, SAFE_METHODS

from contributors.models import Contributor


class IsAuthor(BasePermission):
    message = "You need to be the author!"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if hasattr(obj, "project_id"):
            return obj.project_id.author_user_id == request.user
        else:
            return obj.author_user_id == request.user


class IsContributor(BasePermission):
    message = "You need to be at least a contributor!"

    def has_permission(self, request, view):
        project_pk = view.kwargs.get("project_pk")

        try:
            Contributor.objects.get(user_id=request.user, project_id=project_pk)
        except Contributor.DoesNotExist:
            return False
        return True
