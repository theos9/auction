from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from.models import User, OTP,AuctionsPermission

class BidInline(admin.TabularInline):
    model = AuctionsPermission
    can_delete=False
    extra = 1
@admin.register(User)
class UserAdminPage(UserAdmin):
    change_password_form= AdminPasswordChangeForm
    list_display=['phone_number','national_id','name','family','is_active']
    list_editable=['is_active']
    search_fields=['national_id','phone_number','family']
    list_filter=['is_active']
    ordering = ('phone_number',)
    inlines=[BidInline]
    fieldsets=(
        ('User',{'fields': ('phone_number','password')}),
        ('Personal info',{'fields': ('name','family','national_id','email','card_number','address')}),
        ('Permission',{'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'name', 'family', 'national_id','email', 'password1', 'password2'),
        }),
    )

@admin.register(OTP)
class OtpAdminPage(admin.ModelAdmin):
    list_display=['phone_number','otp','created_at','expires_at']