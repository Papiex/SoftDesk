from django.contrib import admin
from django.urls import path

from projects import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view())
]
