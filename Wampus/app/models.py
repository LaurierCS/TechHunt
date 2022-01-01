# Imports
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

# Profile Model
class Profile(models.Model):

    # Profile Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    # Profile Attributes
    def __str__(self):
        return self.first_name + " " + self.last_name

# Project Model 
class Project(models.Model):

    # Project Fields
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=250, null=True)
    rating = models.IntegerField(default=0, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField('Tag', blank=True)

    # Project Attributes
    def __str__(self):
        return self.name

# Tag Model
class Tag(models.Model):
    
        # Choices for Tag Type
        TYPE_CHOICES = (
            ('T', 'Technology'),
            ('M', 'Miscellaneous'),
        )

        # Tag Fields
        name = models.CharField(max_length=50, null=True)
        date_created = models.DateTimeField(auto_now_add=True)
        type_selection = models.CharField(max_length=1, choices=TYPE_CHOICES)
        projects = models.ManyToManyField('Project', blank=True)
    
        # Tag Attributes
        def __str__(self):
            return self.name

