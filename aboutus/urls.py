from django.urls import path
from .views import ShowAboutUsPageView
urlpatterns = [
    path('',ShowAboutUsPageView.as_view(),name='aboutus-page')
]
