"""Wampus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # For Development

urlpatterns = [
    path('admin/', admin.site.urls), # Do Not Remove
    path('', views.landing_view),
    path('login/', views.login_view),
    path('home/', views.homepage_view),
    path('search/', views.search_projects_view, name='search-projects'),
    path('logout/', views.logout_view),
    path('register/', views.register_view),
    path('delete-project/<slug:project_id>', views.deleteproject_view, name='delete-project'),
    path('project/<slug:project_id>', views.project_view, name='project-page'),
    path('profile/', views.profilepage_view),
    path('about-us/', views.aboutus_view),
    path('create-project/', views.createproject_view),
    path('edit-profile/', views.editprofile_view)
]

"""
Development Purposes (DEBUG = True)
"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()