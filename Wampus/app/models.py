# Imports
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import *
from django.template.defaultfilters import slugify

# Profile Model
class Profile(models.Model):

    # Profile Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    contact_email = models.EmailField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    # Profile Attributes
    def __str__(self):
        try:
            return self.first_name + " " + self.last_name # Return profile name
        except:
            return self.user.username # Return username if profile name is not set

# Project Model 
class Project(models.Model):

    # Project Fields
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    preview_image = models.ImageField(null=True, blank=True)
    rating = models.IntegerField(default=0, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    code_link = models.CharField(max_length=300, null=True, blank=True)

    # Project Attributes
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    # Project Properties
    @property
    def get_comments(self):
        
        comments = self.comment_set.all()
        self.comments = comments

        self.save()
        

# Favorite Model
class Favorite(models.Model):

    # Favorite Fields
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    project = models.OneToOneField('Project', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    # Favorite Attributes
    def __str__(self):
        return self.profile.user.username + "-" + self.project.name

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

# Comment Model
class Comment(models.Model):

    # Comment Fields
    text = models.CharField(max_length=250, null=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)

    # Comment Attributes
    def __str__(self):
        return self.text