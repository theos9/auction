from rest_framework import serializers
from .models import AboutUsModel

class ShowAboutUsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model= AboutUsModel
        fields= ['title','message','image','link','address','coordinates','additional_text']