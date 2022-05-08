from rest_framework import viewsets
from rest_framework.validators import ValidationError

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def perform_create(self, serializer):
        if not self.request.POST["type"]:
            raise ValidationError("You need to specify a type !")
        serializer.save()
