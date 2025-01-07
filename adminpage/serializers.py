from django.contrib.auth.models import Permission, Group
from rest_framework import serializers
from user.models import User , OTP , AuctionsPermission
from auc.models import AuctionModel , Bid ,AuctionImage, Category
from ticket.models import TicketModel
class AuctionsPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionsPermission
        fields = '__all__'
class UserListAdminSerializer(serializers.ModelSerializer):
    auctions_permissions = AuctionsPermissionSerializer(source='auctionspermission_set', many=True,read_only=True)
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

class AuctionsPermissionListAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model= AuctionsPermission
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
        
class AuctionsBidListAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model= Bid
        fields= '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class AuctionsListAdminSerializer(serializers.ModelSerializer):
    bid = AuctionsBidListAdminSerializer(source='bids', many=True,read_only=True)
    class Meta:
        model= AuctionModel
        fields= '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class AuctionImageListAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionImage
        fields= '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class CategoryListAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class TicketListAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketModel
        fields = '__all__'
        extra_kwargs={
            'user':{'required': False,'read_only': True},
            'subject':{'required': False,'read_only': True},
            'message':{'required': False,'read_only': True},
            'created_at':{'required': False,'read_only': True},
            'answered_by':{'required': False,'read_only': True},
            'answer':{'required': False,'read_only': False},
            'answered_at':{'required': False,'read_only': True},
        }
