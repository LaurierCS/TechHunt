from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'dashboard.html')

def login(request):
    return HttpResponse('login')

def registration(request):
    return HttpResponse('registration')

def allFavourites(request):
    return HttpResponse('all favourites')

def settings(request):
    return render(request, 'settings.html')

def userProfile(request):
    return HttpResponse('user profile')

def project(request):
    return HttpResponse('project')

def createProject(request):
    return HttpResponse('create project')

def filteredProjects(request):
    return HttpResponse('filtered projects')