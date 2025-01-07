from django.urls import path
from . import views

urlpatterns = [
    path('users/permissions/lists/', views.PermissionListView.as_view(), name='permissions-list'),
    path('users/groups/lists/', views.GroupListView.as_view(), name='groups-list'),
    path('users/groups/create/', views.GroupCreateView.as_view(), name='groups-create'),
    path('users/groups/<int:pk>', views.GroupDetailView.as_view(), name='groups-detail'),
    path('users/lists/',views.UserListAdminViews.as_view(),name='user_list'),
    path('users/create/',views.UserCreateAdminViews.as_view(),name='user_create'),
    path('users/<int:pk>',views.UserDetailAdminViews.as_view(),name='user_detail'),
    path('otp/lists/',views.OtpListAdminViews.as_view(),name='otp_list'),
    path('otp/create/',views.OtpCreateAdminViews.as_view(),name='otp_create'),
    path('otp/<int:pk>',views.OtpDetailAdminViews.as_view(),name='otp_detail'),
    path('auction/permission/lists/',views.AuctionsPermissionListAdminViews.as_view(),name='AuctionsPermission_list'),
    path('auction/permission/create/',views.AuctionsPermissionCreateAdminViews.as_view(),name='AuctionsPermission_create'),
    path('auction/permission/<int:pk>',views.AuctionsPermissionDetailAdminViews.as_view(),name='AuctionsPermission_detail'),
    path('auction/lists/',views.AuctionsListAdminViews.as_view(),name='Auctions_list'),
    path('auction/create/',views.AuctionsCreateAdminViews.as_view(),name='Auctions_create'),
    path('auction/<int:pk>',views.AuctionsDetailAdminViews.as_view(),name='Auctions_detail'),
    path('bids/lists/',views.AuctionsBidListAdminViews.as_view(),name='bid_list'),
    path('bids/create/',views.AuctionsBidCreateAdminViews.as_view(),name='bid_create'),
    path('bids/<int:pk>',views.AuctionsBidDetailAdminViews.as_view(),name='bid_detail'),
    path('auction/images/lists/',views.AuctionImageListAdminViews.as_view(),name='AuctionImage_list'),
    path('auction/images/create/',views.AuctionImageCreateAdminViews.as_view(),name='AuctionImage_create'),
    path('auction/images/<int:pk>',views.AuctionImageDetailAdminViews.as_view(),name='AuctionImage_detail'),
    path('category/lists/',views.CategoryListAdminViews.as_view(),name='category_list'),
    path('category/create/',views.CategoryCreateAdminViews.as_view(),name='category_create'),
    path('category/<int:pk>',views.CategoryDetailAdminViews.as_view(),name='category_detail'),
    path('ticket/lists/',views.TicketListAdminViews.as_view(),name='ticket_list'),
    path('ticket/create/',views.TicketCreateAdminViews.as_view(),name='ticket_create'),
    path('ticket/<int:pk>',views.TicketDetailAdminViews.as_view(),name='ticket_detail'),
    path('aboutus/lists/',views.AboutUsListAdminViews.as_view(),name='AboutUs_list'),
    path('aboutus/create/',views.AboutUsCreateAdminViews.as_view(),name='AboutUs_create'),
    path('aboutus/<int:pk>',views.AboutUsDetailAdminViews.as_view(),name='AboutUs_detail'),
    

]
