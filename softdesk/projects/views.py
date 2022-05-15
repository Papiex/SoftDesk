from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.validators import ValidationError

from .models import Issue, Project, Comment
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def perform_create(self, serializer):
        if not self.request.POST["type"]:
            raise ValidationError("You need to specify a type !")
        serializer.save()


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])

    def perform_create(self, serializer):
        """Get the project_id with get_object_or_404 method"""
        project = get_object_or_404(Project, id=self.kwargs['project_pk'])
        serializer.save(project=project)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])
    
    def perform_create(self, serializer):
        issue = get_object_or_404(Issue, id=self.kwargs['issue_pk'])
        serializer.save(issue=issue)
