from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
from .models import Post, Category
import markdown
# Create your views here.

def index(request):
    post_list = Post.objects.all()
    context = {
        'post_list' : post_list,
    }
    return render(request, 'blog/index.html', context)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post' : post,
        'form' : form,
        'comment_list' : comment_list,
    }
    return render(request, 'blog/detail.html', context)
