from django.shortcuts import get_object_or_404
from django.db.models.query import QuerySet

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.validators import ValidationError

from .models import Issue, Project, Comment, Contributor
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ContributorSerializer
from .permissions import ProjectPermission


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, ProjectPermission]

    def get_queryset(self) -> QuerySet[Project]:
        """return projects of the connected user"""
        return Project.objects.filter(author_user_id=self.request.user.pk)

class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, ProjectPermission]

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs.get('project_pk'))
    
    def perform_create(self, serializer, *args, **kwargs):
        project = Project.objects.get(pk=self.kwargs.get('project_pk'))
        serializer.save(project=project)


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> QuerySet[Issue]:
        """Get queryset of project issues"""
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
        """Get queryset of project comments"""
        queryset = Comment.objects.filter(issue=self.kwargs['issue_pk'])
        if get_object_or_404(queryset):
            return queryset
    
    def perform_create(self, serializer):
        """Get the issue_id with get_object_or_404 method"""
        issue = get_object_or_404(Issue, id=self.kwargs['issue_pk'])
        serializer.save(issue=issue)
