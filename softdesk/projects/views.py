from rest_framework import mixins, generics, viewsets, renderers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.validators import ValidationError

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def perform_create(self, serializer):
        if not self.request.POST["type"]:
            raise ValidationError("You need to specify a type !")
        serializer.save()















# class ProjectList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     """
#     GET projects list method + POST method 
#     """

#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, *kwargs)
    
#     def post(self, request, *args, **kwargs):
#         if not request.POST["type"]:
#             raise ValidationError("You need to specify a type !")
#         return self.create(request, *args, **kwargs)


# class ProjectDetail(mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   generics.GenericAPIView):
#     """
#     GET project detail method + PUT and DELETE methods
#     """
    
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)