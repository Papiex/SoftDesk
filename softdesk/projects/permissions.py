from rest_framework import permissions

from .models import Project


class AuthorOrContributorProject(permissions.BasePermission):
    """
    Author can update and destroy
    Contributor can retrieve and list projects
    """

    def has_object_permission(self, request, view, obj) -> bool:
        
        if view.action in ['list', 'retrieve']:
            return request.user in obj.contributors.all()
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user == obj.author_user_id


class IssuePermission(permissions.BasePermission):
    """
    Author of issue can update and destroy
    Contributor can create, retrieve and list issues
    """

    def has_object_permission(self, request, view, obj) -> bool:
        
        if view.action in ['list', 'retrieve', 'create']:
            return request.user in obj.project.contributors.all()
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user == obj.author_user_id


class CommentPermission(permissions.BasePermission):
    """
    Author of comment can update and destroy
    Contributor can create, retrieve and list comment
    """

    def has_object_permission(self, request, view, obj) -> bool:
        
        if view.action in ['list', 'retrieve', 'create']:
            return request.user in obj.issue.project.contributors.all()
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user == obj.author_user_id

class ContributorPermission(permissions.BasePermission):
    """
    Author of project can add and destroy contributor
    Contributor can list contributor
    """

    def has_permission(self, request, view) -> bool:

        project = Project.objects.filter(id=view.kwargs['project_pk']).first()
        if view.action in ['list', 'retrieve']:
            return request.user in project.contributors.all()
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user == project.author_user_id
