from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=25)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
