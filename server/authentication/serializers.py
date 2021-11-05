from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)
from authentication.models import CustomUser


class CustomUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "password",
            "full_name",
            "email",
            "created_at",
        ]
