from django.conf import settings
from django.db import models

from projects.models import Project

PERMISSION_CHOICES = [
    ("full", "full"),
    ("limited", "limited"),
]


class Contributor(models.Model):
    user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributor",
    )
    project_id = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name="contributor",
        blank=True,
        null=True,
    )
    permission = models.CharField(
        choices=PERMISSION_CHOICES, default="limited", max_length=255
    )
    role = models.CharField(default="Contributor", max_length=255)

    def __str__(self):
        return (
            str(self.user_id)
            + " is contributor from Project: "
            + self.project_id.title
            + " created by "
            + self.project_id.author_user_id.username
        )
