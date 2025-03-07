from django.db import models
from authors.models import Author
from catagories.models import Category
from tags.models import Tag



class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=100)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(default=True)

