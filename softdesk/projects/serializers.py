from django.forms import CharField
from rest_framework.serializers import ModelSerializer

from projects.models import Project, Issue, Comment


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user_id']
        read_only_fields = ['author_user_id']


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'description',
            'tag',
            'priority',
            'status',
            'project_id',
            'author_user_id',
            'assignee_user_id',
            'created_time']
        read_only_fields = ['author_user_id', 'assignee_user_id', 'created_time']
    

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description', 'issue_id', 'author_user_id', 'created_time']
        read_only_fields = ['author_user_id']