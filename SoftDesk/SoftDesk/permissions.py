from rest_framework.permissions import BasePermission
from rest_framework.generics import get_object_or_404

# from contributors.models import Contributor
from projects.models import Project
from issues.models import Issue


# class IsProjectAuthor(BasePermission):
#     message = "You need to be the author of the project!"

#     def has_permission(self, request, view):
#         try:
#             project = get_object_or_404(Project, pk=view.kwargs["pk"])
#             return project.author_user_id == request.user
#         except KeyError:
#             project = get_object_or_404(Project, pk=view.kwargs["project_pk"])
#             return project.author_user_id == request.user


class IsProjectAuthor(BasePermission):
    message = "You need to be the author of the project!"

    def has_permission(self, request, view):
        project = get_object_or_404(Project, pk=view.kwargs["pk"])
        return project.author_user_id == request.user


class IsContributorAuthor(BasePermission):
    message = "You need to be the author!"

    def has_permission(self, request, view):
        project = get_object_or_404(Project, pk=view.kwargs["project_pk"])
        return project.author_user_id == request.user


class IsIssueAuthor(BasePermission):
    message = "You need to be the author!"

    def has_permission(self, request, view):
        issue = get_object_or_404(Issue, pk=view.kwargs["pk"])
        return issue.author_user_id == request.user


class IsProjectContributor(BasePermission):
    message = "You need to be at least a contributor of the project!"

    def has_permission(self, request, view):
        project = get_object_or_404(Project, pk=view.kwargs["pk"])
        return project in Project.objects.filter(contributor__user_id=request.user)


class IsContributor(BasePermission):
    message = "You need to be at least a contributor of the project!"

    def has_permission(self, request, view):
        project = get_object_or_404(Project, pk=view.kwargs["project_pk"])
        return project in Project.objects.filter(contributor__user_id=request.user)


# class IsIssueContributor(BasePermission):
#     message = "You need to be at least a contributor of the project!"

#     def has_permission(self, request, view):
#         project = get_object_or_404(Project, pk=view.kwargs["project_pk"])
#         return project in Project.objects.filter(contributor__user_id=request.user)


# class IsCommentContributor(BasePermission):
#     message = "You need to be at least a contributor of the project!"

#     def has_permission(self, request, view):
#         project = get_object_or_404(Project, pk=view.kwargs["project_pk"])
#         return project in Project.objects.filter(contributor__user_id=request.user)
