from rest_framework.viewsets import ModelViewSet

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()