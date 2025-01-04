from rest_framework import serializers
from .models import User

class OTPRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)

    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) != 11 or not value.startswith("09"):
            raise serializers.ValidationError('The phone number must have 11 digits and start with 09')
        return value

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
    
    def validate_national_id(self, value):
        if not value.isdigit() or len(value) !=10:
            raise serializers.ValidationError("national id must be 10 digits long and must be a number")
        return value

    def validate_card_number(self, value):
        if not value.isdigit() or len(value) != 16:
            raise serializers.ValidationError('card number must be 16 digits and must be number')
        return value

    def validate_email(self, value):
        if value and '@' not in value:
            raise serializers.ValidationError('email field is invalid')
        return value
    

