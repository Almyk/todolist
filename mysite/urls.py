from django.conf.urls import url, include
from django.contrib import admin
#from .views import home, register # used to import home
from .views import register

urlpatterns = [
    #url(r'^$', home), // using login template, see todolist/urls.py
    url(r'^register/', register),
]
