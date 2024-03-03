from django.db import models

class Blog(models.Model):
    username = models.CharField(max_length = 20)
    blog_title = models.CharField(max_length = 100)
    blog_article = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)

