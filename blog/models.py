from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

#分类表
class Category(models.Model):
    name = models.CharField(max_length=100)

#标签表
class Tag(models.Model):
    name = models.CharField(max_length=100)

#文章表
class Post(models.Model):

    #文章标题
    title = models.CharField(max_length=70)

    #正文字段
    body = models.TextField()

    #文章创建时间和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #文章摘要
    excerpt = models.CharField(max_length=200, blank=True)

    #分类外键和标签外键
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    #文章作者
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_time']

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})