from rest_framework import serializers
from .models import User,OTP
from django.utils import timezone
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'name', 'family', 'email','national_id', 'card_number', 'address']

    def validate_national_id(self, value):
        if not value.isdigit() or len(value) !=10:
            raise serializers.ValidationError("national id must be 10 digits long and must be a number")
        return value

    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) != 11 or not value.startswith("09"):
            raise serializers.ValidationError("The phone number must have 11 digits and start with 09")
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("this phone number exists")
        return value

    def validate_card_number(self, value):
        if not value.isdigit() or len(value) != 16:
            raise serializers.ValidationError('card number must be 16 digits and must be number')
        return value

    def validate_email(self, value):
        if value and '@' not in value:
            raise serializers.ValidationError('email field is invalid')
        return value

class OTPRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)

    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) != 11 or not value.startswith("09"):
            raise serializers.ValidationError('The phone number must have 11 digits and start with 09')
        return value

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        phone_number = data.get('phone_number')
        otp = data.get('otp')

        if not User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("This phone number is not registered.")

        try:
            otp_record = OTP.objects.get(phone_number=phone_number)
        except OTP.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP.")

        if otp_record.otp != otp:
            raise serializers.ValidationError("Incorrect OTP.")

        if otp_record.expires_at < timezone.now():
            raise serializers.ValidationError("OTP has expired.")

        return data
    
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
    

