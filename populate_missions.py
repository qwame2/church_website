import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'church_website.settings')
django.setup()

from django.contrib.auth.models import User
from game.models import Mission, UserMission, Activity

# Create default missions
missions = [
    {'title': 'Complete 1 Solo Quiz', 'reward_points': 50, 'target_count': 1, 'icon_class': 'ri-check-line'},
    {'title': 'Challenge 1 Friend', 'reward_points': 100, 'target_count': 1, 'icon_class': 'ri-team-line'},
    {'title': 'Daily Bible Trivia', 'reward_points': 30, 'target_count': 1, 'icon_class': 'ri-flashlight-line'},
]

for m_data in missions:
    Mission.objects.get_or_create(title=m_data['title'], defaults=m_data)

# Assign missions to existing users if they don't have them
users = User.objects.all()
all_missions = Mission.objects.all()

for user in users:
    for mission in all_missions:
        UserMission.objects.get_or_create(user=user, mission=mission)
    
    # Create some mock activity for visualization
    if not Activity.objects.filter(user=user).exists():
        Activity.objects.create(
            user=user,
            title='Joined Scripture Champions',
            description='Welcome to the divine quest for knowledge!',
            icon_class='ri-user-add-line',
            icon_bg_color='bg-blue-100',
            icon_text_color='text-blue-600'
        )

print("Missions and Activities populated successfully!")
