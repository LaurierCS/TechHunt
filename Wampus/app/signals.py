# Imports
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# Create a Profile for every new User
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    
    if created:
        Profile.objects.create(user=instance)

# Update the Profile every time a User is updated
@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    
    if created == False:
        instance.profile.save()
    

    