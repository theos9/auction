from django.contrib import admin
from . import models


@admin.register(models.AuctionImage)
class PicsAuctionAdmin(admin.ModelAdmin):
    list_display=['image_tag','id']
    readonly_fields = ['image_tag','id']
    fieldsets = (
        ('pictures', {
            'fields': ('image','image_tag','id')
        }),
    )

class BidInline(admin.TabularInline):
    model = models.Bid
    readonly_fields=['bidder','bid_amount','bid_time']
    can_delete=True
    extra = 0
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
@admin.register(models.AuctionModel)
class AuctionAdmin(admin.ModelAdmin):
    list_display=['title','category','start_date','end_date','status','id']
    list_editable=['status']
    filter_horizontal = ('images',)
    fieldsets = (
        ('Auction title', {
            'fields': ('title','description','category','images')
        }),
        ('price', {
            'fields': ('starting_price','current_price','increment_step')
        }),
        ('time', {
            'fields': ('start_date','end_date')
        }),
        ('Participant details', {
            'fields': ('winner','bidders_count','offer_count')
        }),
        ('status', {
            'fields': ('status',)
        }),
    )
    readonly_fields = ['offer_count','current_price','winner','bidders_count']
    inlines = [BidInline] 

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','parent']


