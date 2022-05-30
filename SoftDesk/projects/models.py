from django.conf import settings
from django.db import models


class Project(models.Model):
    options = (
        ("back end", "back end"),
        ("front end", "front end"),
        ("iOS", "iOS"),
        ("Android", "Android"),
    )

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(choices=options, default="back end", max_length=255)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="author_project",
    )

    def __str__(self):
        return self.title
