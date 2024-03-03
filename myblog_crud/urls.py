from django.urls import path
from .views import BlogListCreateAPIView, BlogRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('blog_crud/', BlogListCreateAPIView.as_view(), name='blog-list-create'),

    path('blog_crud/<int:pk>/', BlogRetrieveUpdateDeleteAPIView.as_view(), name='blog-retrieve-update-destroy'),
]