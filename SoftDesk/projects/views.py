from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from SoftDesk.permissions import IsAuthor

from .models import Project
from contributors.models import Contributor
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self, *args, **kwargs):
        contributors = Contributor.objects.filter(user_id=self.request.user)
        projects = [contributor.project_id.id for contributor in contributors]
        return Project.objects.filter(id__in=projects)
