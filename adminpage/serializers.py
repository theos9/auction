from django.contrib.auth.models import Permission, Group
from rest_framework import serializers
from user.models import User , OTP

class UserListAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class PermissionListAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class GroupListAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        extra_kwargs = {
            'permissions':{'required':True},
            'name':{'required':True},
            }
        
class OtpListAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model= OTP
        fields = '__all__'