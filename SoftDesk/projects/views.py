from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from SoftDesk.permissions import IsProjectAuthor, IsProjectContributor

from .models import Project
from contributors.models import Contributor
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAuthenticated()]
        if self.action == "list":
            permission_classes = [IsAuthenticated()]
        if self.action == "retrieve":
            permission_classes = [IsAuthenticated(), IsProjectContributor()]
        if self.action == "update":
            permission_classes = [IsAuthenticated(), IsProjectAuthor()]
        if self.action == "destroy":
            permission_classes = [IsAuthenticated(), IsProjectAuthor()]
        return permission_classes

    def get_queryset(self, *args, **kwargs):
        contributors = Contributor.objects.filter(user_id=self.request.user)
        projects = [contributor.project_id.id for contributor in contributors]
        return Project.objects.filter(id__in=projects)
