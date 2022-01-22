def search_projects(request):

    query = request.GET.get('query') # Get the search query

    # If the query is empty, return all projects
    if query == '':
        return Project.objects.all()

    search_results = Project.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(profile__user__username__icontains=query) |
        Q(tags__name__icontains=query)
    )

    # Otherwise, return the queried projects by name, description, tags, categories or users
    return search_results