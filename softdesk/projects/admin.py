from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'type', 'author_user_id')


admin.site.register(Project, ProjectAdmin)
