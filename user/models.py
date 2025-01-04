from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
import random

class UserManager(BaseUserManager):
    def create_user(self, phone_number, national_id, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Entering the phone number is required')
        if not national_id:
            raise ValueError('Entering the national id is required')

        user = self.model(phone_number=phone_number, national_id=national_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, national_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, national_id, password, **extra_fields)

    
class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=11, unique=True,verbose_name='phone number')
    name=models.CharField(max_length=20,verbose_name='name',null=True,blank=False)
    family=models.CharField(max_length=20,verbose_name='last name',null=True,blank=False)
    email=models.EmailField(verbose_name='email',null=True,blank=True)
    national_id=models.CharField(verbose_name='national id',max_length=10,unique=True,null=True,blank=False)
    card_number=models.CharField(max_length=16,verbose_name='card number',null=True,blank=True)
    address=models.CharField(max_length=255,verbose_name='address',null=True,blank=True)
    is_active = models.BooleanField(default=1,verbose_name='active/inactive')
    is_staff = models.BooleanField(default=False,verbose_name='staff')
    is_superuser = models.BooleanField(default=False,verbose_name='owner')

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
        verbose_name = 'User'
        verbose_name_plural ='Users'
        
    def __str__(self):
        return f"{self.name} {self.family}"
    
class OTP(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    class Meta:
        verbose_name = 'Otp'
        verbose_name_plural ='Otp'
    
    def is_valid(self):
        if timezone.now() > self.expires_at:
            if OTP.objects.filter(id=self.id).exists():
                self.delete()
            return False
        return True

    def generate_expiration(self):
        self.expires_at = timezone.now() + timezone.timedelta(minutes=15)

class AuctionsPermission(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='user')
    auctions=models.ForeignKey('auc.AuctionModel',on_delete=models.CASCADE,verbose_name='auctions')
    permission=models.BooleanField(default=False,verbose_name='permission')
    class Meta:
        verbose_name = 'Auction access'
        verbose_name_plural = 'accesses'
    def __str__(self):
        return f'{self.auctions} - {self.permission}'