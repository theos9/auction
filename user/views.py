from rest_framework import status, generics
from .serializers import RegisterSerializer,OTPRequestSerializer
import random
from rest_framework.mixins import CreateModelMixin
from .sms import send_sms
from rest_framework.response import Response
from .models import User,OTP
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(generics.GenericAPIView,CreateModelMixin):
    serializer_class = RegisterSerializer
    def GenerateOtp(self):
        return str(random.randint(100000, 999999))
    def get(self, request, *args, **kwargs):
        serializer=OTPRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        phone_number=serializer.validated_data['phone_number']
        if User.objects.filter(phone_number=phone_number).exists():
            return Response({'error':'this phone number is exists'},status.HTTP_406_NOT_ACCEPTABLE)
        otp_code=self.GenerateOtp()
        expires_at=timezone.now()+timezone.timedelta(minutes=15)
        OTP.objects.update_or_create(phone_number=phone_number,defaults={'otp':otp_code,'expires_at':expires_at})
        param={
                    "name": "CODE",
                    "value": f"{otp_code}"
                }
        api='hWiijhqcGxXsSGgXNV1IrvnD0yjD9vGVe'
        send_sms(str(phone_number),608,param,api)
        print(otp_code)
        return Response({'message':'otp send successful'})


    def post(self, request, *args, **kwargs):
        data=request.data
        phone_number=data.get('phone_number')
        otp=data.get('otp')
        if not OTP.objects.filter(phone_number=phone_number).exists():
            return Response({'error':'otp not found for this phone number'},status.HTTP_404_NOT_FOUND)
        otp_entry= OTP.objects.get(phone_number=phone_number)
        if otp_entry.otp != otp or otp_entry.expires_at < timezone.now():
            return Response({'error':'this otp invalid or expired'},status.HTTP_400_BAD_REQUEST)
        serializer= self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user= serializer.save()
        otp_entry.delete()
        refresh=RefreshToken.for_user(user)
        return Response({'full_name':f'{user.name} {user.family}','access':str(refresh.access_token),'refresh':str(refresh),'message':'user create successful'})


