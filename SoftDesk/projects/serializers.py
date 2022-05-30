from rest_framework import serializers

from .models import Project
from contributors.models import Contributor


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        project.author_user_id = self.context["request"].user
        project.save()
        Contributor.objects.create(
            user_id=self.context["request"].user,
            project_id=project,
            permission="full",
            role="Author",
        )
        return project
