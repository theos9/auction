from django.contrib.auth.models import Permission, Group
from rest_framework.response import Response
from rest_framework import status , generics
from rest_framework.permissions import IsAdminUser
from user.models import User , OTP
from . import serializers 
class PermissionListView(generics.ListAPIView):
    queryset = Permission.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = serializers.PermissionListAdminSerializer

class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = serializers.GroupListAdminSerializer

class GroupCreateView(generics.CreateAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = serializers.GroupListAdminSerializer
class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = serializers.GroupListAdminSerializer
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

class OtpListAdminViews(generics.ListAPIView):
    queryset = OTP.objects.all()
    permission_classes=[IsAdminUser]
    serializer_class = serializers.OtpListAdminSerializer

class OtpCreateAdminViews(generics.CreateAPIView):
    queryset = OTP.objects.all()
    permission_classes=[IsAdminUser]
    serializer_class = serializers.OtpListAdminSerializer

class OtpDetailAdminViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = OTP.objects.all()
    permission_classes=[IsAdminUser]
    serializer_class = serializers.OtpListAdminSerializer