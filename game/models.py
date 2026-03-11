from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    rank = models.CharField(max_length=50, default="Beginner")
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, default='ri-gamepad-line')
    button_text = models.CharField(max_length=50, default='Start Now')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class GameSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_sessions')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    points_earned = models.IntegerField(default=0)
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game.title} - {self.score}"

class Mission(models.Model):
    title = models.CharField(max_length=200)
    reward_points = models.IntegerField(default=50)
    target_count = models.IntegerField(default=1)
    icon_class = models.CharField(max_length=100, default='ri-flag-line')

    def __str__(self):
        return self.title

class UserMission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_missions')
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    current_count = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    reset_at = models.DateTimeField(null=True, blank=True)

    def progress_percentage(self):
        if self.mission.target_count == 0: return 100
        return min(int((self.current_count / self.mission.target_count) * 100), 100)

    def __str__(self):
        return f"{self.user.username} - {self.mission.title}"

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=50, default='ri-check-line')
    icon_bg_color = models.CharField(max_length=20, default='bg-green-100')
    icon_text_color = models.CharField(max_length=20, default='text-green-600')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Activities"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.title}"

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=100, default='Qualification Phase')
    end_date = models.DateTimeField()
    qualification_points = models.IntegerField(default=1000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def days_left(self):
        from django.utils import timezone
        diff = self.end_date - timezone.now()
        return max(diff.days, 0)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
    else:
        Profile.objects.create(user=instance)
