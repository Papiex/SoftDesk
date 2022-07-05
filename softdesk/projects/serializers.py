from rest_framework.serializers import ModelSerializer

from .models.comment import Comment
from .models.contributor import Contributor
from .models.issue import Issue
from .models.project import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description", "type", "author_user_id"]
        read_only_fields = ["author_user_id"]

    def create(self, validated_data) -> Project:
        """
        create project and add the author in the contributors with the ALL permission
        """
        user = self.context["request"].user
        project = Project.objects.create(author_user_id=user, **validated_data)

        Contributor.objects.create(
            user=project.author_user_id,
            project=project,
            permission="ALL",
            role="AUTHOR",
        )
        project.save()
        return project


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["user", "project", "permission", "role"]
        read_only_fields = ["project"]


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "status",
            "project_id",
            "author_user_id",
            "assignee_user_id",
            "created_time",
        ]
        read_only_fields = ["author_user_id", "assignee_user_id", "created_time"]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "description", "issue_id", "author_user_id", "created_time"]
        read_only_fields = ["author_user_id"]
