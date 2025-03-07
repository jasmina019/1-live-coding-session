from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name= models.CharField(max_length=100)
    description =models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return  self.name

    def __str__(self, *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)


