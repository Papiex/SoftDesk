from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from projects import views


router = DefaultRouter()
router.register(r"projects", views.ProjectViewSet, basename="projects")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
