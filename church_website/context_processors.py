# context_processors.py
from django.conf import settings

def ad_settings(request):
    return {
        'ads_enabled': settings.ADS_ENABLED,
        # You could add logic to show/hide ads based on user roles
        'show_ads': not request.user.is_authenticated or not request.user.is_staff
    }