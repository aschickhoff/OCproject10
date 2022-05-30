from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from SoftDesk.permissions import IsIssueAuthor, IsContributor
from .models import Issue
from projects.models import Project

from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAuthenticated(), IsContributor()]
        if self.action == "list":
            permission_classes = [IsAuthenticated(), IsContributor()]
        if self.action == "retrieve":
            permission_classes = [IsAuthenticated(), IsContributor()]
        if self.action == "update":
            permission_classes = [IsAuthenticated(), IsIssueAuthor()]
        if self.action == "destroy":
            permission_classes = [IsAuthenticated(), IsIssueAuthor()]
        return permission_classes

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs["project_pk"])

    def perform_create(self, serializer):
        project_pk = Project.objects.get(pk=self.kwargs["project_pk"])
        serializer.save(
            project_id=project_pk,
            author_user_id=self.request.user,
        )
