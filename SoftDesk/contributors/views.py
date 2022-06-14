from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from SoftDesk.permissions import IsAuthor

from .models import Contributor
from .serializers import ContributorSerializer


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self, *args, **kwargs):
        return Contributor.objects.filter(project_id=self.kwargs["project_pk"])
