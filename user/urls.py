from django.urls import path
from .views import LoginRegisterView,UpdateUserProfileView

urlpatterns = [
    path("LoginRegister/", LoginRegisterView.as_view(), name='login'),
    path('edit/',UpdateUserProfileView.as_view(),name='update')
]