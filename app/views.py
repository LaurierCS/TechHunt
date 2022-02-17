# Imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, CreateProjectForm, EditProfileForm, ProfileForm, CommentForm
from django.db.models import Q
from .models import Project, Tag, Profile, Favorite, Comment
from .query import search_projects

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

        else:  # If the user is not authenticated, show an error message
            messages.error(request, 'Invalid username or password')

    return render(request, template_name)

def logout_view(request):

    logout(request)
    
    return redirect('/login/')

def register_view(request):

    template_name = 'register.html'

    form = RegisterForm(request.POST) # Create form object

    if form.is_valid():    
        user = form.save() # If the form is valid, save the user
        login(request, user) # Log the user in
        return redirect('/homepage/') # Redirect to homepage 

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

    context = {
        'projects': projects,
        'profile': profile,
        'favorites': favorites,
        'tags': tags,
        'popular_projects': popular_projects
    }

    template_name = 'homepage.html'

    return render(request, template_name, context)

def search_projects_view(request):
    user = request.user # Get the user object
     
    profile = Profile.objects.get(user=user) # Get the user's profile

    if request.method == "GET":
        return redirect('/homepage/')

    if request.method == "POST":
        search_value = request.POST['search_value']
        search_results = search_projects(search_value) # Get search results

    context = {
        'profile': profile,
        'search_value': search_value,
        'search_results': search_results
    }

    template_name = 'search-projects.html'

    return render(request, template_name, context)

def profilepage_view(request):

    # If the user is not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect('/login/')

    user = request.user # Get the user object
     
    profile = Profile.objects.get(user=user) # Get the user's profile
    projects = Project.objects.filter(profile=profile)  # Get the user's projects
    favorites = Favorite.objects.filter(profile=profile)  # Get the user's favorites

    context = {
        'profile': profile,
        'projects': projects,
        'favorites': favorites
    }

    template_name = 'profile.html'

    return render(request, template_name, context)


def project_view(request, project_id):
    user = request.user # Get the user object
     
    profile = Profile.objects.get(user=user) # Get the user's profile
    project = Project.objects.get(id=project_id)

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = request.POST.get('text')
            comment = Comment.objects.create(text = text, profile = profile, project = project)
            comment.save()

    context = {
        'profile': profile,
        'project': project,
        'form': form
    }

    template_name = 'project.html'

    return render(request, template_name, context)

@login_required(login_url='/login/')
def createproject_view(request):

    # Get current user profile
    profile = request.user.profile
    form = CreateProjectForm()

    if request.method == 'POST':
        form = CreateProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.profile = profile
            project.save()
            return redirect("/project/" + str(project.id))
            
    context = {
        'profile': profile,
        'form': form 
    }

    template_name = 'create-project.html'

    return render(request, template_name, context)

@login_required(login_url='/login/')
def updateproject_view(request, pk):
    
    # Get current user profile
    profile = request.user.profile
    project = Project.objects.get(pk=pk)
    form = CreateProjectForm(instance=project)

    if request.method == 'POST':
        form = CreateProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            project = form.save()
            project.profile = profile
            project.save()
            
    context = {'form': form }       

    template_name = 'project.html' # Template might need to change?

    return render(request, template_name, context)

@login_required(login_url='/login/')
def deleteproject_view(request, project_id):
    user = request.user # Get the user object
     
    profile = Profile.objects.get(user=user) # Get the user's profile
    project = Project.objects.get(id=project_id)

    if project.profile == profile:
        if request.method == 'POST':
            project.delete()
            return redirect('/profile')
    else:
        return redirect('/homepage/')

    template_name = 'delete-project.html'

    context = {
        'project': project,
        'profile': profile
    }

    return render(request, template_name, context)

def aboutus_view(request):
    user = request.user # Get the user object
     
    profile = Profile.objects.get(user=user) # Get the user's profile

    context = {
        'profile': profile
    }

    template_name = 'about.html'

    return render(request, template_name, context)

def editprofile_view(request):
    # Get current user profile
    profile = request.user.profile
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            user_info = form.save()
            profile.contact_email = user_info.email
            profile_form.save()
            return redirect("/profile/")
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'profile': profile,
        'form': form,
        'profile_form': profile_form
    }
    template_name = 'edit-profile.html'

    return render(request, template_name, context)

def landing_view(request):

    template_name = 'landing.html'

    return render(request, template_name)
