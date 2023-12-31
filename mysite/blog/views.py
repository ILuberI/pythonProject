from django.shortcuts import render

# Create your views here.
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_py('-created_at')
    return render(request, 'blog/post_list.html', {'posts', posts})