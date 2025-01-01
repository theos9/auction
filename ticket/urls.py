from django.urls import path
from .views import CreateTicketView, ListUserTicketsView

urlpatterns = [
    path('', ListUserTicketsView.as_view(), name='list_tickets'),
    path('create/', CreateTicketView.as_view(), name='create_ticket'),
]
