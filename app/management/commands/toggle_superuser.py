from django.core.management.base import BaseCommand
from app.models import User

class Command(BaseCommand): 
    def add_arguments(self, parser): 
        parser.add_argument("-u", "--user", type=str)

    def handle(self, *args, **kwargs):
        username = kwargs["user"]
        u = User.objects.get(username=username)
        u.is_superuser = not u.is_superuser
        u.save()

