# Inside models.py
from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Comment(models.Model):
    comment = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now =True)
    # Notice the association made with ForeignKey for a one to many relationship
    # There can be many comments to one blog

    blog = models.ForeignKey(Blog, related_name = "comments")
class Admin(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    blogs = models.ManyToManyField(Blog, related_name = "admins")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

'''
second_author = Author.objects.get(id=2)
my_book = list(second_author.books) => queryset (for loop)
my_book[0].title

# second case :
mybook = second_author.books (my book  is an object os QuerySet class) => It will support iteration for using loop
book
for book  in mybook:


'''