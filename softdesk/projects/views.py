from django.shortcuts import get_object_or_404
from django.db.models.query import QuerySet

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Issue, Project, Comment, Contributor
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ContributorSerializer
from .permissions import AuthorOrReadOnly, ContributorPermission

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, AuthorOrReadOnly]

    def get_queryset(self) -> QuerySet[Project]:
        """return projects of the connected user"""
        return Project.objects.filter(contributors=self.request.user.pk)


class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, ContributorPermission]

    def get_queryset(self):
        """return the contributors list of the project"""
        return Contributor.objects.filter(project=self.kwargs.get('project_pk'))

    def create(self, request, *args, **kwargs) -> Response:
        """
        Add contributor to a project
        If user added already in this project return 400
        """
        project = Project.objects.get(pk=self.kwargs.get('project_pk'))
        serializer = ContributorSerializer(data=request.data)
        user = request.data['user']

        if Contributor.objects.filter(user=user).filter(project=project).exists():
            return Response('This user is already a contributor of this project', status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                serializer.save(project=project)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, AuthorOrReadOnly]

    def get_queryset(self) -> QuerySet[Issue]:
        """Return issues of the project"""
        return Issue.objects.filter(project=self.kwargs['project_pk'])

    def perform_create(self, serializer):
        """Get the project_id with get_object_or_404 method"""
        project = get_object_or_404(Project, id=self.kwargs['project_pk'])
        assignee_user_id = self.request.user
        serializer.save(
            project=project,
            author_user_id=self.request.user,
            assignee_user_id=assignee_user_id)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, AuthorOrReadOnly]

    def get_queryset(self) -> QuerySet[Comment]:
        """Return the comments of an issue"""
        queryset = Comment.objects.filter(issue=self.kwargs['issue_pk'])
        if get_object_or_404(queryset):
            return queryset
    
    def perform_create(self, serializer):
        """Get the issue_id with get_object_or_404 method"""
        issue = get_object_or_404(Issue, id=self.kwargs['issue_pk'])
        serializer.save(issue=issue, author_user_id=self.request.user)
