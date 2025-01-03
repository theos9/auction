from django.db import models
from user.models import User
from django.utils.html import format_html
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True, verbose_name='Category Name')
    parent = TreeForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='children', 
        verbose_name='Parent Category'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class AuctionImage(models.Model):
    image = models.ImageField(upload_to='data/auction_images/', verbose_name='image', null=True, blank=True)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def image_tag(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="100" height="100" />')
        return 'No image available'
    image_tag.short_description = "preview"

    def __str__(self):
        return str(self.id)
class AuctionModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    description = models.TextField(verbose_name='description')
    category = TreeForeignKey(
        Category, 
        on_delete=models.PROTECT, 
        related_name='auctions', 
        verbose_name='Category',
        null=True,
        blank=True
    )
    starting_price = models.FloatField(verbose_name='starting price')
    current_price = models.FloatField(verbose_name='current price', default=0.0)
    increment_step = models.FloatField(verbose_name='increment step', default=50000)
    start_date = models.DateTimeField(verbose_name='start date')
    end_date = models.DateTimeField(verbose_name='end date')
    images = models.ManyToManyField(AuctionImage, related_name='auctions', verbose_name='images', blank=True)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='won_auctions', verbose_name='winner',
                               null=True, blank=True)
    bidders = models.ManyToManyField(User, through='Bid', related_name='bids', verbose_name='bidders')
    status = models.BooleanField(default=True, verbose_name='status')

    class Meta:
        verbose_name = 'auction'
        verbose_name_plural = 'auctions'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        now = timezone.now()
        if not self.current_price:
            self.current_price = self.starting_price
        if self.end_date < now and self.winner is None or (self.status==False and self.winner is None and self.bidders.count()>1):
            self.determine_winner()
        super().save(*args, **kwargs)

    def determine_winner(self):
        highest_bid = self.bids.order_by('-bid_amount').first()
        if highest_bid:
            self.winner = highest_bid.bidder
            self.status = False
            self.save()

    
    def bids_count(self):
        return self.bidders.distinct().count()
    
    bids_count.short_description='Number of bidders'
    def offer_count(self):
        return self.bidders.count()
    
    offer_count.short_description='Number of offers'
    def __str__(self):
        return self.title

class Bid(models.Model):
    auction = models.ForeignKey(AuctionModel, on_delete=models.CASCADE, related_name='bids', verbose_name='auction')
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='bidder')
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='bid amount')
    bid_time = models.DateTimeField(auto_now_add=True, verbose_name='bid time')

    class Meta:
        verbose_name = 'bid'
        verbose_name_plural = 'bids'

    def save(self, *args, **kwargs):
        if self.bid_amount <= self.auction.current_price:
            raise ValueError("Bid amount must be greater than the current price.")
        if not self.bid_time:
            self.bid_time = timezone.now()
        super().save(*args, **kwargs)
        self.auction.current_price = self.bid_amount
        self.auction.save()

    def __str__(self):
        return f'{self.bidder} - {self.bid_amount}'

class user(models.Model):
    name=models.CharField
