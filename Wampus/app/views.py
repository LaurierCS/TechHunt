from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.db.models import Q
from .models import Project, Category, Tag, Profile, Favorite, Comment
from .query import search_projects


def login_view(request):

    template_name = 'login.html'

    # If the user is already logged in, redirect to homepage
    if request.user.is_authenticated:
        return redirect('/')

    # Get user input from the login form
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(username=username, password=password)

        # If the user is authenticated, log them in
        if user is not None:
            login(request, user)
            return redirect('/')

        else:  # If the user is not authenticated, show an error message
            messages.error(request, 'Invalid username or password')

    return render(request, template_name)


def register_view(request):

    template_name = 'register.html'

    form = RegisterForm(request.POST) # Create form object

    if form.is_valid():    
        user = form.save() # If the form is valid, save the user
        login(request, user) # Log the user in
        return redirect('/') # Redirect to homepage 

    context = {'form': form }

    return render(request, template_name, context)


def homepage_view(request):

    if not request.user.is_authenticated: # If the user is not logged in, redirect to login page
        return redirect('/login/')

    user = request.user # Get the user object
     
    profile = Profile.objects.get(user=user)  # Get the user's profile
    projects = Project.objects.filter(profile=profile)  # Get the user's projects
    favorites = Favorite.objects.filter(profile=profile)  # Get the user's favorites
    tags = Tag.objects.all() # Get all tags
    popular_projects = Project.objects.all().order_by('-rating')[:5] # Get most popular projects
    search_results = search_projects(request) # Get search results

    context = {
        'projects': projects,
        'profile': profile,
        'favorites': favorites,
        'tags': tags,
        'popular_projects': popular_projects,
        'search_results': search_results
    }

    template_name = 'homepage.html'

    return render(request, template_name, context)

def profilepage_view(request):

    # If the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect('/login/')

    object1 = """Some object queried from the Database, 
                maybe a project or set of project objects"""

    context = {
        # You place objects in here that you want to bring
        # to the front end. You do it just by adding them
        # to this dictionary commonly called context -
        # simply store key and value pairs
        # For example:
        'object1': object1
    }

    template_name = 'profile.html'

    return render(request, template_name, context)


def project_view(request):
    object1 = """Some object queried from the Database, 
                maybe a project or set of project objects"""

    context = {
        # You place objects in here that you want to bring
        # to the front end. You do it just by adding them
        # to this dictionary commonly called context -
        # simply store key and value pairs
        # For example:
        'object1': object1
    }

    template_name = 'project.html'

    return render(request, template_name, context)


def aboutus_view(request):
    object1 = """Some object queried from the Database, 
                maybe a project or set of project objects"""

    context = {
        # You place objects in here that you want to bring
        # to the front end. You do it just by adding them
        # to this dictionary commonly called context -
        # simply store key and value pairs
        # For example:
        'object1': object1
    }

    template_name = 'about.html'

    return render(request, template_name, context)


def createproject_view(request):
    object1 = """Some object queried from the Database, 
                maybe a project or set of project objects"""

    context = {
        # You place objects in here that you want to bring
        # to the front end. You do it just by adding them
        # to this dictionary commonly called context -
        # simply store key and value pairs
        # For example:
        'object1': object1
    }

    template_name = 'create-project.html'

    return render(request, template_name, context)
