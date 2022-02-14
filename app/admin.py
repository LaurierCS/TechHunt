# Imports
from django.contrib import admin
from .models import Profile, Project, Tag, Favorite, Comment

# Profile Model Admin 
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# Register Profile Model
admin.site.register(Profile, ProfileAdmin)

# Project Model Admin
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# Register Project Model
admin.site.register(Project, ProjectAdmin)

# Register Favorite Model
admin.site.register(Favorite)

# Register Tag Model
admin.site.register(Tag)

# Register Comment Model
admin.site.register(Comment)