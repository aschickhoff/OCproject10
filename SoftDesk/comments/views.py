from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from SoftDesk.permissions import IsAuthor, IsContributor
from .models import Comment
from issues.models import Issue

from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthor, IsContributor]

    def get_queryset(self, *args, **kwargs):
        return Comment.objects.filter(issue_id=self.kwargs["issue_pk"])

    def perform_create(self, serializer):
        issue_pk = Issue.objects.get(pk=self.kwargs["issue_pk"])
        serializer.save(
            issue_id=issue_pk,
            author_user_id=self.request.user,
        )
