from .models import Project
from django.db.models import Q

def search_projects(query):

    if query is None:
        return Project.objects.all()

    search_results = Project.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(profile__user__username__icontains=query) |
        Q(tags__name__icontains=query)
    )

    # Otherwise, return the queried projects by name, description, tags, categories or users
    return search_results