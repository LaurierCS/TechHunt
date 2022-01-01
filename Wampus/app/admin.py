# Imports
from django.contrib import admin
from .models import Profile, Project, Tag

# Register Profile Model
admin.site.register(Profile)

# Register Project Model
admin.site.register(Project)

# Register Tag Model
admin.site.register(Tag)
