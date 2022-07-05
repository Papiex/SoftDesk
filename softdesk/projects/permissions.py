from rest_framework.generics import get_object_or_404
from rest_framework import permissions

from .models import Project


class AuthorOrReadOnly(permissions.BasePermission):
    """
    Author can update and destroy
    Contributor can retrieve and list projects
    """

    message = "You don't have the permission to do this !"

    def has_permission(self, request, view):
        if view.kwargs.get('project_pk') is not None:
            project = get_object_or_404(Project, id=view.kwargs.get('project_pk'))
            return request.user in project.contributors.all()
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author_user_id


class ContributorPermission(permissions.BasePermission):
    """
    Author of project can add and destroy contributor
    Contributor can list contributor
    """
    message = "You don't have the permission to do this !"

    def has_permission(self, request, view) -> bool:
        project = Project.objects.filter(id=view.kwargs['project_pk']).first()
        if view.action in ['list', 'retrieve']:
            return request.user in project.contributors.all()

        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user == project.author_user_id