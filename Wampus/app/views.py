from django.shortcuts import render, redirect, get_object_or_404

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

    template_name = 'dashboard.html'

    return render(request, template_name, context)


def login_view(request):
    context = {}
    template_name = 'login.html'

    return render(request, template_name, context)


def register_view(request):
    context = {}
    template_name = 'register.html'

    return render(request, template_name, context)


def homepage_view(request):
    context = {}
    template_name = 'homepage.html'

    return render(request, template_name, context)


def profilepage_view(request):
    context = {}
    template_name = 'profile.html'

    return render(request, template_name, context)


def project_view(request):
    context = {}
    template_name = 'project.html'

    return render(request, template_name, context)
