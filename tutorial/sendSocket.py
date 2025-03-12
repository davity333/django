from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Proyect
import json

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        projects = await self.get_projects()
        data = [{'name': p.name, 'date': p.date, 'description': p.description, 'technologies': p.technologies, 'allie': p.allie.name if p.allie else None} for p in projects]
        await self.send(text_data=json.dumps({
            'projects': data
        }))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            data = json.loads(text_data)
            name = data.get('name')
            date = data.get('date')
            description = data.get('description')
            technologies = data.get('technologies')
            allie_id = data.get('allie_id')
            message = await self.save_project(name, date, description, technologies, allie_id)
            await self.send(json.dumps({
                'message': message
            }))

    @database_sync_to_async
    def save_project(self, name, date, description, technologies, allie_id):
        allie = Allies.objects.get(id=allie_id) if allie_id else None
        project = Proyect.objects.create(name=name, date=date, description=description, technologies=technologies, allie=allie)
        return f"Project '{project.name}' saved successfully."

    @database_sync_to_async
    def get_projects(self):
        return list(Proyect.objects.all().order_by('name'))
