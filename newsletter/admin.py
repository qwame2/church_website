# newsletter/admin.py
from django.contrib import admin
from .models import Subscriber, WebsiteContent

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed') 
    search_fields = ('email',)  


class WebsiteContentAdmin(admin.ModelAdmin):
    list_display = ('page_name',)  # Display page name in the list
    search_fields = ('page_name',)  # Search content by page name

# Register the models with custom admins
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(WebsiteContent, WebsiteContentAdmin)
