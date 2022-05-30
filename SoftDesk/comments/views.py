from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from SoftDesk.permissions import IsContributor, IsContributorAuthor
from .models import Comment
from issues.models import Issue

from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAuthenticated(), IsContributor()]
        if self.action == "list":
            permission_classes = [IsAuthenticated(), IsContributor()]
        if self.action == "retrieve":
            permission_classes = [IsAuthenticated(), IsContributor()]
        if self.action == "update":
            permission_classes = [IsAuthenticated(), IsContributorAuthor()]
        if self.action == "destroy":
            permission_classes = [IsAuthenticated(), IsContributorAuthor()]
        return permission_classes

    def get_queryset(self):
        return Comment.objects.filter(issue_id=self.kwargs["issue_pk"])

    def perform_create(self, serializer):
        issue_pk = Issue.objects.get(pk=self.kwargs["issue_pk"])
        serializer.save(
            issue_id=issue_pk,
            author_user_id=self.request.user,
        )
