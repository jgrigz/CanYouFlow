from rest_framework import generics

# serializers 
from authentication.serializers import CustomUserSerializer

# models
from authentication.models import CustomUser


class CreateCustomUser(generics.CreateAPIView):
    '''create new user'''
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUsersView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer