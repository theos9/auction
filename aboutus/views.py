from rest_framework import generics
from .serializers import ShowAboutUsPageSerializer
from .models import AboutUsModel

class ShowAboutUsPageView(generics.ListAPIView):
    queryset=AboutUsModel.objects.all()
    serializer_class=ShowAboutUsPageSerializer
