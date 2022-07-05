from django.contrib import admin

from .models import comment, issue, contributor, project


class ProjectAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'type', 'author_user_id')


class IssueAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'description',
        'tag',
        'priority',
        'status',
        'author_user_id',
        'assignee_user_id',
        'created_time')


class CommentAdmin(admin.ModelAdmin):

    list_display = ('description', 'author_user_id', 'created_time')


class ContributorAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'project', 'permission', 'role')


admin.site.register(project.Project, ProjectAdmin)
admin.site.register(issue.Issue, IssueAdmin)
admin.site.register(comment.Comment, CommentAdmin)
admin.site.register(contributor.Contributor, ContributorAdmin)