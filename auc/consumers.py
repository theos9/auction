import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from django.shortcuts import get_object_or_404
from .models import AuctionModel
from .serializers import AuctionSerializer
from asgiref.sync import sync_to_async

class AuctionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.auction_id = self.scope['url_route']['kwargs']['auction_id']
        self.auction_group_name = f'auction_{self.auction_id}'
        self.channel_layer = get_channel_layer()
        
        await self.channel_layer.group_add(
            self.auction_group_name,
            self.channel_name
        )
        await self.accept()

        auction = await sync_to_async(get_object_or_404)(AuctionModel, id=self.auction_id, status=True)
        serializer = AuctionSerializer(auction)
        serialized_data = await sync_to_async(lambda: serializer.data)()
        await self.send(text_data=json.dumps(serialized_data))

    async def disconnect(self, close_code):
        if hasattr(self, 'channel_layer'):
            await self.channel_layer.group_discard(
                self.auction_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            await self.channel_layer.group_send(
                self.auction_group_name,
                {
                    'type': 'auction_update',
                    'message': data
                }
            )
            await self.update_auction_data()
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'error': 'Invalid JSON format'
            }))

    async def auction_update(self, event):
        await self.send(text_data=json.dumps(event["message"]))
