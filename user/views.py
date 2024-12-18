from rest_framework import status, generics
from .serializers import RegisterSerializer,OTPRequestSerializer
import random
from rest_framework.mixins import CreateModelMixin
from .sms import send_sms
from rest_framework.response import Response
from .models import User,OTP
from django.utils import timezone

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
        api='hWiijhqcGxXsSGgXNV1IrvnD0yjD9vGVeH9XwM83g8S4s9gz2Q9yOFyy0gJMPL5i'
        send_sms(str(phone_number),608162,param,api)
        print(otp_code)
        return Response({'message':'otp send successful'})


    def post(self, request, *args, **kwargs):
        pass