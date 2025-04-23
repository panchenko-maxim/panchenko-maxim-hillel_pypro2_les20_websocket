import json
import re
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
from django.core.exceptions import PermissionDenied


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

