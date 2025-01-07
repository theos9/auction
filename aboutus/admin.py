from django.contrib import admin
from .models import AboutUsModel

@admin.register(AboutUsModel)
class AboutUsAdmin(admin.ModelAdmin):
    list_display=['title','message','image_tag']
    readonly_fields = ['image_tag',]
    fieldsets = (
        ('title,message', {
            'fields': ('title','message')
        }),
        ('image', {
            'fields': ('image','image_tag')
        }),
        ('etc', {
            'fields': ('link','address','coordinates','additional_text')
        }),
        
    )
    