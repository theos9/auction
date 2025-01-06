from django.contrib.auth.models import Permission, Group
from rest_framework.response import Response
from rest_framework import status , generics
from rest_framework.permissions import IsAdminUser
from user.models import User
from . import serializers 
class PermissionListView(generics.ListAPIView):
    queryset = Permission.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = serializers.PermissionSerializer

class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = serializers.GroupSerializer

class GroupCreateView(generics.CreateAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = serializers.GroupSerializer
class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = serializers.GroupSerializer
class UserListAdminViews(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = serializers.UserListAdminSerializer

class UserCreateAdminViews(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = serializers.UserListAdminSerializer 
class UserDetailAdminViews(generics.RetrieveUpdateDestroyAPIView):
    queryset= User.objects.all()
    permission_classes= [IsAdminUser]
    serializer_class= serializers.UserListAdminSerializer
