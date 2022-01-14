from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.db.models import Q
from .models import Project, Category, Tag, Profile, Favorite, Comment

def login_view(request):

    template_name = 'login.html'

    # If the user is already logged in, redirect to homepage
    if request.user.is_authenticated:
        return redirect('/homepage/')

    # Get user input from the login form
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(username=username, password=password)

        # If the user is authenticated, log them in
        if user is not None:
            login(request, user)
            return redirect('/homepage/')
        
        else: # If the user is not authenticated, show an error message
            messages.error(request, 'Invalid username or password')
    
    return render(request, template_name)


def register_view(request):
    
    template_name = 'register.html'

    # Create form object
    form = RegisterForm(request.POST)

    # If the form is valid, save the user
    if form.is_valid():
        user = form.save()

        # Log the user in
        login(request, user)

        # Redirect to homepage    
        return redirect('/homepage/')
    
    context = {'form': form}
    
    return render(request, template_name, context)

def homepage_view(request):
    
    # If the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect('/login/')

    # Get the current user
    user = request.user

    # Get the user's profile
    profile = Profile.objects.get(user=user)

    # Get the user's projects
    projects = Project.objects.filter(profile=profile)

    # Get the user's favorites
    favorites = Favorite.objects.filter(profile=profile)

    # Get all tags
    tags = Tag.objects.all()

    # Get most popular projects 
    popular_projects = Project.objects.all().order_by('-rating')[:5] 

    # Define a function to search all projects
    def search_projects(request):
            
        # Get the search query
        query = request.GET.get('query') # Change the tag in the HTML to fit the name of the query or it will throw error

        # If the query is empty, return all projects
        if query == '':
            return Project.objects.all()

        search_results = Project.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(profile__user__username__icontains=query) |
            Q(tags__name__icontains=query) |
            Q(categories__name__icontains=query)
        )

        # Otherwise, return the queried projects by name, description, tags, categories or users
        return search_results

    # Search projects using search bar
    search_results = search_projects(request)

    context = {
        'search_results': search_results,
        'projects': projects,
        'profile': profile,
        'favorites': favorites,
        'tags': tags
    }

    template_name = 'homepage.html'

    return render(request, template_name, context)


def profilepage_view(request):

    # If the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect('/login/')

    object1 =  """Some object queried from the Database, 
                maybe a project or set of project objects"""
    
    context = {
        #You place objects in here that you want to bring 
        # to the front end. You do it just by adding them
        # to this dictionary commonly called context -
        # simply store key and value pairs
        # For example:
        'object1':object1
    }

    template_name = 'profile.html'

    return render(request, template_name, context)


def project_view(request):
    object1 =  """Some object queried from the Database, 
                maybe a project or set of project objects"""
    
    context = {
        #You place objects in here that you want to bring 
        # to the front end. You do it just by adding them
        # to this dictionary commonly called context -
        # simply store key and value pairs
        # For example:
        'object1':object1
    }

    template_name = 'project.html'

    return render(request, template_name, context)

def aboutus_view(request):
    object1 =  """Some object queried from the Database, 
                maybe a project or set of project objects"""
    
    context = {
        #You place objects in here that you want to bring 
        # to the front end. You do it just by adding them
        # to this dictionary commonly called context -
        # simply store key and value pairs
        # For example:
        'object1':object1
    }

    template_name = 'about.html'

    return render(request, template_name, context)

def createproject_view(request):
    object1 =  """Some object queried from the Database, 
                maybe a project or set of project objects"""
    
    context = {
        #You place objects in here that you want to bring 
        # to the front end. You do it just by adding them
        # to this dictionary commonly called context -
        # simply store key and value pairs
        # For example:
        'object1':object1
    }

    template_name = 'create-project.html'

    return render(request, template_name, context)