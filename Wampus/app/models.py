# Imports
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

# Profile Model
class Profile(models.Model):

    """
    Description
    --------------------------------------------------
    Represents a Profile within the Models.
    A Profile is a user of the Wampus application.
    
    Model Fields
    --------------------------------------------------
    user: OneToOneField
    first_name : str
    last_name : str
    bio : str
    location : str
    date_created: DateTimeField

    Model Attributes
    --------------------------------------------------
    __str__():
        Returns the string representation of Profile name.

    Author
    --------------------------------------------------
    Aidan Traboulay
    """

    # Profile Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    bio = models.TextField(max_length=500, null=True)
    location = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    # Profile Attributes
    def __str__(self):
        return self.first_name + " " + self.last_name

# Project Model 
class Project(models.Model):

    """
    Description
    --------------------------------------------------
    Represents a Project within the Models.
    A Project is a project that a user has created.

    Model Fields
    --------------------------------------------------
    name : str
    description : str
    rating : int
    date_created: DateTimeField
    profile: ForeignKey

    Model Attributes
    --------------------------------------------------
    __str__():
        Returns the string representation of Project name.
    
    Author
    --------------------------------------------------
    Aidan Traboulay
    """

    # Project Fields
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=250, null=True)
    rating = models.IntegerField(default=0, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    # Project Attributes
    def __str__(self):
        return self.name

