import os
import django
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'church_website.settings')
django.setup()

from game.models import Tournament

# Create a June Tournament (since we're in March, let's make it a "Tournament of Champions")
Tournament.objects.get_or_create(
    name='March Scripture Tournament',
    defaults={
        'status': 'Qualification Phase',
        'end_date': timezone.now() + timedelta(days=15),
        'qualification_points': 500,
        'active': True
    }
)

print("Tournament populated successfully!")
