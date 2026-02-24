from django.db import models

# Create your models here.
from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# newsletter/models.py
from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class WebsiteContent(models.Model):
    page_name = models.CharField(max_length=255, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.page_name
