from django.shortcuts import render

def homepage(request, pk):
    context = {}
    template_name = 'dashboard.html'
    return render(request, template_name, context)

def login(request, pk):
    context = {}
    template_name = '<templatename>.html'
    return render(request, template_name, context)

def registration(request, pk):
    context = {}
    template_name = '<templatename>.html'
    return render(request, template_name, context)

def userProfile(request, pk):
    context = {}
    template_name = '<templatename>.html'
    return render(request, template_name, context)

def project(request, pk):
    context = {}
    template_name = '<templatename>.html'
    return render(request, template_name, context)

"""

def createProject(request, pk):
    context = {}
    template_name = '<templatename>.html'
    return render(request, template_name, context)

def filteredProjects(request, pk):
    context = {}
    template_name = '<templatename>.html'
    return render(request, template_name, context)

def allFavourites(request, pk):
    context = {}
    template_name = '<templatename>.html'
    return render(request, template_name, context)

def settings(request, pk):
    context = {}
    template_name = 'settings.html'
    return render(request, template_name, context)

"""
