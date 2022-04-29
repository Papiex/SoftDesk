from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from projects.views import ProjectViewset


router = routers.SimpleRouter()
router.register('projects', ProjectViewset, basename='project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
