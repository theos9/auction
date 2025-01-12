from rest_framework import serializers
from .models import User

class OTPRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
    otp = serializers.CharField(max_length=6)
    
    def create(self, validated_data):
        phone_number = validated_data['phone_number']
        user = User.objects.create(phone_number=phone_number)
        return user
    
class UpdateProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields = ['phone_number','name','family','email','national_id','card_number','address']
        extra_kwargs = {
            'phone_number': {'required': False,'read_only':True},
            'name': {'required': False},
            'family': {'required': False},
            'email': {'required': False},
            'national_id': {'required': False},
            'address': {'required': False},
            'card_number': {'required': False},
        }
    

