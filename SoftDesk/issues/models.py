from django.conf import settings
from django.db import models

from projects.models import Project

PRIORITY_CHOICES = [
    ("LOW", "LOW"),
    ("MEDIUM", "MEDIUM"),
    ("HIGH", "HIGH"),
]

TAG_CHOICES = [
    ("BUG", "BUG"),
    ("TASK", "TASK"),
    ("ENHANCEMENT", "ENHANCEMENT"),
]


STATUS_CHOICES = [
    ("To-Do", "To-Do"),
    ("In-Progress", "In-Progress"),
    ("Completed", "Completed"),
]


class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    tag = models.CharField(choices=TAG_CHOICES, default="BUG", max_length=255)
    priority = models.CharField(choices=PRIORITY_CHOICES, default="LOW", max_length=255)
    project_id = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, blank=True, null=True
    )
    status = models.CharField(choices=STATUS_CHOICES, default="To-Do", max_length=255)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="author_user",
    )
    assignee_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="assignee"
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            self.title
            + " from "
            + str(self.author_user_id)
            + " for Project: "
            + self.project_id.title
        )
