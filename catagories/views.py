from rest_framework import generics
from .models import Category


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
