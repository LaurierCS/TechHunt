# Imports
from django.contrib import admin
from .models import Profile, Project, Tag, Favorite

# Register Profile Model
admin.site.register(Profile)

# Register Project Model
admin.site.register(Project)

# Register Favorite Model
admin.site.register(Favorite)

# Register Tag Model
admin.site.register(Tag)

