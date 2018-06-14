from django.db import models

# Create your models here.

class Course_Manager(models.Manager):
    def validate(self, post_data):
        if len(post_data['name']) < 2:
            return False
        if len(post_data['desc']) < 5:
            return False
        return True

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = Course_Manager()
