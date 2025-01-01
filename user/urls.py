from django.urls import path
from .views import RegisterView,LoginView,UpdateUserProfileView

urlpatterns = [
    path("register/",RegisterView.as_view(),name='register'),
    path("login/", LoginView.as_view(), name='login'),
    path('edit/',UpdateUserProfileView.as_view(),name='update')
]