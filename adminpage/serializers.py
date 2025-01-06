from django.contrib.auth.models import Permission, Group
from rest_framework import serializers
from user.models import User

class UserListAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        extra_kwargs = {
            'permissions':{'required':True},
            'name':{'required':True},
            }