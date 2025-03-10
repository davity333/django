import json 
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Service 
class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        services = await self.getService()
        data = [{'name': S.name, 'description': S.description, 'technologies': S.technologies} for S in services]
        await self.send(text_data=json.dumps({
            'services': data
        }))
    async def disconnect(self, close_code):
        pass
    async def receive(self, text_data=None, bytes_data=None): 
        if text_data: 
         Json = json.loads(text_data)
         nombre = Json.get('name')
         tecnologias = Json.get('technologies')
         descripcion = Json.get('description')
         mensaje = await self.guardarService(nombre, tecnologias, descripcion)
         await self.send(json.dumps({
             'message': mensaje
         }))
    @database_sync_to_async
    def guardarService(self, name,technologies, description): 
       return Service.objects.create(name= name,technologies=technologies,  description=description)
    @database_sync_to_async
    def getService(self):
        return list(Service.objects.all().order_by('name'))