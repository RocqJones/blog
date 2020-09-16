"""
    This has been created after configuring a path inside mysite.urls
    This will control what to display on '127.0.0.1:8000/'
    Here we will be importing Django's function path and all of our views from the blog application.
    NOTE: The application will be created shortly
    But we can add the url and the proceed to creating the views.
    - This pattern will tell Django that 'views.post_list' is the right place to go if someone enters 
      your website 'http://127.0.0.1:8000/'
    - name='post_list', is the name of the URL that will be used to identify the view
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list')
]