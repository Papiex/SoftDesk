from rest_framework.serializers import ModelSerializer, CharField, EmailField
from rest_framework.validators import UniqueValidator, ValidationError
from django.contrib.auth.password_validation import validate_password

from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class RegisterSerializer(ModelSerializer):
    email = EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )

    password = CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

        def create(self, validated_data):
            user = User.objects.create_user(validated_data['email'], validated_data['password'])
            user.first_name = validated_data['first_name']
            user.last_name = validated_data['last_name']
            user.save()
            return user
