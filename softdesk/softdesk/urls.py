from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from authentication.views import RegisterView
from projects import views

router = DefaultRouter()
router.register(r"projects", views.ProjectViewSet)

project_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
project_router.register(r"issues", views.IssueViewSet, basename="issues")
project_router.register(r"users", views.ContributorViewSet, basename="users")

issue_router = routers.NestedSimpleRouter(project_router, r"issues", lookup="issue")
issue_router.register(r"comments", views.CommentViewSet, basename="comments")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("", include(project_router.urls)),
    path("", include(issue_router.urls)),
    path("signup/", RegisterView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="obtain_tokens"),
    path("login/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
]
