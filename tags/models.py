from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)

