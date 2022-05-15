from cgitb import lookup
from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter

from projects import views


router = DefaultRouter()
router.register(r"projects", views.ProjectViewSet)

project_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
project_router.register(r"issues", views.IssueViewSet, basename="issues")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(project_router.urls)),
]
