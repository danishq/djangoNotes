
from django.urls import path
from . import views
urlpatterns = [
    path('appone',views.A_app,name='A_app'),
    path('tailwindSetup', views.tailwindSetup, name='tailwindSetup')
]