from django.conf import settings
from django.db import models

from issues.models import Issue


class Comment(models.Model):
    description = models.CharField(max_length=255)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    issue_id = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE, blank=True, null=True
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            "Comment from "
            + str(self.author_user_id)
            + " on Issue: "
            + self.issue_id.title
        )
