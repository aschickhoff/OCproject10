from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from SoftDesk.permissions import IsContributorAuthor

from .models import Contributor
from .serializers import ContributorSerializer


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [
                IsAuthenticated(),
                IsContributorAuthor(),
            ]  # done, need to ask for KeyError
        if self.action == "list":
            permission_classes = [IsAuthenticated(), IsContributorAuthor()]
        if self.action == "retrieve":
            permission_classes = [IsAuthenticated(), IsContributorAuthor()]
        if self.action == "destroy":
            permission_classes = [IsAuthenticated(), IsContributorAuthor()]
        return permission_classes

    def get_queryset(self):
        return Contributor.objects.filter(project_id=self.kwargs["project_pk"])
