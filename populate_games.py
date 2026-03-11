import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'church_website.settings')
django.setup()

from game.models import Game

games = [
    {
        'title': 'Solo Quiz',
        'description': 'Test your knowledge at your own pace with adaptive levels.',
        'category': 'Education',
        'icon_class': 'ri-user-line',
        'button_text': 'Start Now'
    },
    {
        'title': 'Challenge Friend',
        'description': 'Compete head-to-head with friends and climb the ranks.',
        'category': 'Social',
        'icon_class': 'ri-team-line',
        'button_text': 'Challenge'
    },
    {
        'title': 'Daily Trivia',
        'description': "Answer today's special set of questions for bonus points!",
        'category': 'Daily',
        'icon_class': 'ri-flashlight-line',
        'button_text': 'Play Daily'
    },
    {
        'title': 'Verse Memorizer',
        'description': 'Unscramble and memorize key verses from the Bible.',
        'category': 'Scripture',
        'icon_class': 'ri-book-read-line',
        'button_text': 'Practice'
    },
    {
        'title': 'Biblical Word Search',
        'description': 'Find names of prophets, cities, and miracles hidden in the grid.',
        'category': 'Games',
        'icon_class': 'ri-search-eye-line',
        'button_text': 'Find Words'
    },
    {
        'title': 'Parable Puzzle',
        'description': "Match Jesus' parables to their deep spiritual meanings.",
        'category': 'Games',
        'icon_class': 'ri-puzzle-line',
        'button_text': 'Solve Puzzle'
    }
]

for game_data in games:
    Game.objects.get_or_create(
        title=game_data['title'],
        defaults=game_data
    )

print("Games populated successfully!")
