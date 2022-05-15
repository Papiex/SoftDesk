from dataclasses import fields
from rest_framework.serializers import ModelSerializer

from projects.models import Project, Issue


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user_id']
        read_only_fields = ['author_user_id']


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status', 'author_user_id', 'assignee_user_id', 'created_time']
        read_only_fields = ['author_user_id', 'assignee_user_id', 'created_time']