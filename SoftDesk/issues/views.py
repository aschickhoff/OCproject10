from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from SoftDesk.permissions import IsAuthor, IsContributor
from .models import Issue
from projects.models import Project

from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsAuthor, IsContributor]

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs["project_pk"])

    def perform_create(self, serializer):
        project_pk = Project.objects.get(pk=self.kwargs["project_pk"])
        serializer.save(
            project_id=project_pk,
            author_user_id=self.request.user,
        )
