from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import CharField, EmailField, ModelSerializer
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True, validators=[validate_password])
    email = EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def create(self, validated_data) -> User:
        """
        Get the user with post validated data
        set user.is_active to true and save
        """
        user = self.Meta.model(**validated_data)
        user.set_password(validated_data["password"])
        user.is_active = True
        user.save()
        return user
