from django.urls import path
from .views import AuctionListView, AuctionDetailView, CreateBidView

urlpatterns = [
    path('', AuctionListView.as_view(), name='auction-list'),
    path('<int:pk>/', AuctionDetailView.as_view(), name='auction-detail'),
    path('<int:auction_id>/bids/', CreateBidView.as_view(), name='create-bid'),
]