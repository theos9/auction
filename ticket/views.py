from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import TicketModel
from .serializers import CreateTicketSerializer ,TicketSerializer

class CreateTicketView(generics.CreateAPIView):
    serializer_class=CreateTicketSerializer
    permission_classes=[IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}
    
class ListUserTicketsView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TicketModel.objects.filter(user=self.request.user)
