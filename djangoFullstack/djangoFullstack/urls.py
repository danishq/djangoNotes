"""
URL configuration for djangoFullstack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.main,name='main'),
    path('djangoApp/',include('djangoApp.urls')), # we need to import 'include' which we are doing in line 18 path,include
    #here '' means the root page which is localhost:8000 => '' , and views.main will go to views.py file and render and here we are mainly routing the page to the url link . this name='main' is always unique and no to path can have same name and also we need to import views by writing from .( current directory ) import views


    path("__reload__/", include("django_browser_reload.urls")),
]
