from django.shortcuts import get_object_or_404
from django.db.models.query import QuerySet

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.validators import ValidationError

from .models import Issue, Project, Comment
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> QuerySet[Project]:
        """return projects of the connected user"""
        return Project.objects.filter(author_user_id=self.request.user.pk)
    
    def perform_create(self, serializer):
        if not self.request.POST["type"]:
            raise ValidationError("You need to specify a type !")
        serializer.save(author_user_id=self.request.user)


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> QuerySet[Issue]:
        queryset = Issue.objects.filter(project=self.kwargs['project_pk'])
        if get_object_or_404(queryset):
            return queryset

    def perform_create(self, serializer):
        """Get the project_id with get_object_or_404 method"""
        project = get_object_or_404(Project, id=self.kwargs['project_pk'])
        serializer.save(project=project)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> QuerySet[Comment]:
        queryset = Comment.objects.filter(issue=self.kwargs['issue_pk'])
        if get_object_or_404(queryset):
            return queryset
    
    def perform_create(self, serializer):
        """Get the issue_id with get_object_or_404 method"""
        issue = get_object_or_404(Issue, id=self.kwargs['issue_pk'])
        serializer.save(issue=issue)
