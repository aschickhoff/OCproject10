from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Contributor.objects.all(),
                fields=["user_id", "project_id"],
                message="The user is already contributing to the project.",
            )
        ]
