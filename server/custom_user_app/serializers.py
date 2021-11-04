
from rest_framework.relations import SlugRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedModelSerializer,
    StringRelatedField,
)
from custom_user_app.models import CustomUser

class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "password",
            "full_name",
            "email",
            "created_at",
        ]