from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
import random

class UserManager(BaseUserManager):
    def create_user(self, phone_number, national_id, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('شماره تماس باید وارد شود')
        if not national_id:
            raise ValueError('کد ملی باید وارد شود')

        user = self.model(phone_number=phone_number, national_id=national_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, national_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, national_id, password, **extra_fields)

    
class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=11, unique=True,verbose_name='شماره تماس')
    name=models.CharField(max_length=20,verbose_name='نام',null=False,blank=False)
    family=models.CharField(max_length=20,verbose_name='نام خانوادگی',null=False,blank=False)
    email=models.EmailField(verbose_name='ایمیل',unique=True,null=False,blank=False)
    national_id=models.CharField(verbose_name='کد ملی',max_length=10,unique=True,null=False,blank=False)
    card_number=models.CharField(max_length=16,verbose_name='شماره کارت',null=False,blank=False)
    address=models.CharField(max_length=255,verbose_name='ادرس')
    is_active = models.BooleanField(default=1,verbose_name='فعال/غیر فعال')
    is_staff = models.BooleanField(default=False,verbose_name='کارمند')
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name','family', 'national_id']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
    )

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural ='کاربرها'
        
    def __str__(self):
        return f"{self.name} {self.family}"
    
class OTP(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    class Meta:
        verbose_name = 'رمز یکبار مصرف'
        verbose_name_plural ='رمز یکبار مصرف'
    
    def is_valid(self):
        if timezone.now() > self.expires_at:
            if OTP.objects.filter(id=self.id).exists():
                self.delete()
            return False
        return True

    def generate_expiration(self):
        self.expires_at = timezone.now() + timezone.timedelta(minutes=15)