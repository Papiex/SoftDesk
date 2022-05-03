from rest_framework.serializers import ModelSerializer, SerializerMethodField

from projects.models import Project


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user_id']