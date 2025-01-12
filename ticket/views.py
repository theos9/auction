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
    def perform_create(self, serializer):
        user = self.request.user
        if not user.email:
            return Response({'email': 'You have not provided an email'}, status=status.HTTP_400_BAD_REQUEST)
        
        subject = self.request.data.get('subject')
        message = self.request.data.get('message')
        if not subject:
            return Response({'subject': 'Subject is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not message:
            return Response({'message': 'Message is required'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    
class ListUserTicketsView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TicketModel.objects.filter(user=self.request.user)
