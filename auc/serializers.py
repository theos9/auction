from rest_framework import serializers
from .models import AuctionModel,Bid,AuctionImage, Category

class AuctionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionImage
        fields = ['id', 'image']
class Categorys(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class AuctionSerializer(serializers.ModelSerializer):
    images = AuctionImageSerializer(many=True, read_only=True)
    category= Categorys(read_only=True)

    class Meta:
        model = AuctionModel
        fields = ['id', 'title', 'description','category', 'starting_price', 'current_price', 'increment_step', 'start_date', 'end_date', 'status', 'winner', 'images', 'bidders_count', 'offer_count']

class BidSerializers(serializers.ModelSerializer):
    class Meta:
        model= Bid
        fields=['bid_amount']
    def create(self, validated_data):
        auction_id = self.context['auction_id']
        auction = AuctionModel.objects.get(id=auction_id)
        bidder = self.context['request'].user
        bid = Bid.objects.create(auction=auction, bidder=bidder, **validated_data)
        return bid
    
class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'children']

    def get_children(self,obj):
        if obj.children.exists():
            return CategorySerializer(obj.children.all(), many=True).data
        return None
