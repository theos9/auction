from django.urls import path
from . import views

urlpatterns = [
    path('users/permissions/lists/', views.PermissionListView.as_view(), name='permissions-list'),
    path('users/groups/lists/', views.GroupListView.as_view(), name='groups-list'),
    path('users/groups/create/', views.GroupCreateView.as_view(), name='groups-create'),
    path('users/groups/<int:pk>', views.GroupDetailView.as_view(), name='groups-detail'),
    path('users/lists/',views.UserListAdminViews.as_view(),name='user_list'),
    path('users/create/',views.UserCreateAdminViews.as_view(),name='user_create'),
    path('users/<int:pk>',views.UserDetailAdminViews.as_view(),name='user_detail')
]
