from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .serializers import OTPRequestSerializer,LoginSerializer,UpdateProfileSerializer
from .otp import OtpGenerator
from rest_framework.mixins import CreateModelMixin
from .sms import send_sms
from rest_framework.response import Response
from .models import User,OTP
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

class LoginRegisterView(generics.GenericAPIView,CreateModelMixin):
    serializer_class = LoginSerializer
    def get(self,request,*args,**kwargs):
        try:
            serializer = OTPRequestSerializer(data=request.query_params)
            serializer.is_valid(raise_exception=True)
            phone_number=serializer.validated_data['phone_number']
            if not phone_number.isdigit() or len(phone_number) != 11 or not phone_number.startswith("09"):
                return Response({'error':'The phone number must have 11 digits and start with 09'},status.HTTP_400_BAD_REQUEST)
            otp_code=OtpGenerator.GenerateOtp()
            expires_at = timezone.now() + timezone.timedelta(minutes=15)
            OTP.objects.update_or_create(phone_number=phone_number, defaults={'otp': otp_code, 'expires_at': expires_at})
            param={
                "name": "CODE",
                "value": f"{otp_code}"
            }
            api='hWiijhqcGxXsSGgXNV1IrvnD0yjD9vGVe'
            # send_sms(str(phone_number),608,param,api)
            print(otp_code)
            return Response({'message':'otp send successful'},status.HTTP_200_OK)
        except:
            return Response({'error':'syntax error'},status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            phone_number = serializer.validated_data['phone_number']
            otp = serializer.validated_data['otp']
            if not phone_number.isdigit() or len(phone_number) != 11 or not phone_number.startswith("09"):
                return Response({'error':'The phone number must have 11 digits and start with 09'},status.HTTP_400_BAD_REQUEST)
            otp_record = OTP.objects.filter(phone_number=phone_number).first()
            if not otp_record:
                return Response({'error':"Invalid OTP."},status.HTTP_400_BAD_REQUEST)
            elif otp_record.otp != otp:
                return Response({'error':'Incorrect OTP.'},status.HTTP_400_BAD_REQUEST)
            elif otp_record.expires_at < timezone.now():
                return Response({'error':'OTP has expired.'},status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(phone_number=phone_number).exists():
                user = User.objects.get(phone_number=phone_number)
            else:
                user= serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            OTP.objects.get(phone_number=phone_number).delete()
            return Response({
                'message': 'Login or register successful',
                'access_token': access_token,
                'refresh_token': refresh_token,
            }, status=status.HTTP_200_OK)
        except:
            return Response({'error':'syntax error'},status.HTTP_500_INTERNAL_SERVER_ERROR)
class UpdateUserProfileView(generics.RetrieveUpdateAPIView):
    queryset= User.objects.all()
    serializer_class = UpdateProfileSerializer
    permission_classes=[IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    def perform_update(self, serializer):
        data = self.request.data
        
        national_id = data.get('national_id')
        if national_id and (not national_id.isdigit() or len(national_id) != 10):
            return Response({'national_id': 'National ID must be 10 digits long and must be a number'})
        
        card_number = data.get('card_number')
        if card_number and (not card_number.isdigit() or len(card_number) != 16):
            return Response({'card_number': 'Card number must be 16 digits long and must be a number'})
        
        email = data.get('email')
        if email and '@' not in email:
            return Response({'email': 'Email field is invalid'})
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    

