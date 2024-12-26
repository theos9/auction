from rest_framework import serializers
from .models import AuctionModel,Bid,AuctionImage

class AuctionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionImage
        fields = ['id', 'image']

class AuctionSerializer(serializers.ModelSerializer):
    images = AuctionImageSerializer(many=True, read_only=True)
    bids_count = serializers.IntegerField(read_only=True)
    offer_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = AuctionModel
        fields = ['id', 'title', 'description', 'starting_price', 'current_price', 'increment_step', 'start_date', 'end_date', 'status', 'winner', 'images', 'bids_count', 'offer_count']

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
