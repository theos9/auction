from rest_framework import serializers
from .models import TicketModel

class CreateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=TicketModel
        fields= ['subject','message']
    
    def create(self, validated_data):
        user=self.context['request'].user
        return TicketModel.objects.create(user=user,**validated_data)
    
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketModel
        fields = ['id', 'subject', 'message', 'created_at', 'is_answered', 'answer']