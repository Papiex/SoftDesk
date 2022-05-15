from django.contrib import admin
from projects.models import Project, Issue


class ProjectAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'type', 'author_user_id')


class IssueAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'tag', 'priority', 'status', 'author_user_id', 'assignee_user_id', 'created_time')


class CommentAdmin(admin.ModelAdmin):

    list_display = ('description', 'author_user_id', 'created_time')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
