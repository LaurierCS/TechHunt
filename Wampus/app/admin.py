# Imports
from django.contrib import admin
from .models import Profile, Project, Favorite

# Register Profile Model
admin.site.register(Profile)

# Register Project Model
admin.site.register(Project)

# Register Favorite Model
admin.site.register(Favorite)
