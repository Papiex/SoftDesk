from .serializers import UserSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class RegisterView(GenericAPIView):

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs) -> Response:
        """Create user and return data entered"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({'detail': 'User created !'})
    

