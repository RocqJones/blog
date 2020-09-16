"""
    A model in Django is a special kind of object – it is saved in the database. 
    A database is a collection of data. 
    This is a place in which you will store information about users, your blog posts, etc. 
    We will be using a SQLite database to store our data. This is the default Django database adapter
"""
from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):

    # NOTE: 'models' is an object
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # we will get a text (string) with a Post title
    def __str__(self):
        return self.title

    # Now we create tables for our Model in the database