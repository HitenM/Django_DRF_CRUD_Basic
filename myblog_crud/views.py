from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Blog
from .serializers import BlogSerializer

class BlogListCreateAPIView(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

class BlogRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()