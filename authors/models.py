from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    bio = models.TextField()


