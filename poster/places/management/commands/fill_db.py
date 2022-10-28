from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=settings.ADMIN_USERNAME)
            user.delete()
        except User.DoesNotExist:
            print('Database is empty')

        User.objects.create_superuser(
            username=settings.ADMIN_USERNAME,
            email=settings.ADMIN_EMAIL,
            password=settings.ADMIN_PASSWORD
        )
