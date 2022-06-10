from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }


    def create(self, validated_data) -> User:
        """
        Get the user with post validated data
        set user.is_active to true and save
        """
        user = self.Meta.model(**validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user
