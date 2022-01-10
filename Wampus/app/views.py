from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

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