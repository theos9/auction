from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status , generics
from datetime import timedelta
from user.models import AuctionsPermission
from django.shortcuts import get_object_or_404
from .models import AuctionModel,Category
from .serializers import AuctionSerializer,BidSerializers, CategorySerializer
from django.utils import timezone

class AuctionListView(generics.ListAPIView):
    queryset=AuctionModel.objects.all()
    serializer_class= AuctionSerializer

class AuctionDetailView(generics.RetrieveAPIView):
    queryset = AuctionModel.objects.all()
    serializer_class = AuctionSerializer

class CreateBidView(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,auction_id):
        now = timezone.now()
        user=request.user
        auction= get_object_or_404(AuctionModel,id=auction_id)


        if not auction.status or (auction.start_date>now) or (auction.end_date<now):
            return Response({'error':'This auction is not active'},status=status.HTTP_423_LOCKED)
        
        auction_permission = AuctionsPermission.objects.filter(user=user, auctions=auction).first()
        if not auction_permission or not auction_permission.permission:
            return Response({'error':'Your access to the auction is not connected or blocked'},status=status.HTTP_423_LOCKED)



        if 'bid_amount' in request.data and float(request.data['bid_amount'])< auction.current_price + auction.increment_step:
            return Response({'error':'The bid amount is less than the minimum allowed'},status=status.HTTP_400_BAD_REQUEST)
        
        time_remaining =auction.end_date-now
        if time_remaining <= timedelta(hours=1):
            auction.end_date += timedelta(hours=1)
            auction.save()

        serializer = BidSerializers(data=request.data, context={'auction_id': auction_id, 'request': request})
        if serializer.is_valid():
            serializer.save()
            auction.current_price= serializer.validated_data['bid_amount']
            auction.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None).order_by('name')
    serializer_class = CategorySerializer
        