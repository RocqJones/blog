from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)

"""
    Create super user
    $ python3 manage.py createsuperuser
    Example: admin, admin@administrator.com, Password: amonone33
"""