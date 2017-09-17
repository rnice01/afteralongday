from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
# Create your views here.

def index(request):
    post = Post.objects.latest('published')
    return render(request, 'blogs.html', {'post': post})

def like_comment(request):
    if request.is_ajax():
        post_id = request.POST.get('post_id')
        if Post.objects.filter(id=post_id, favorited=request.user).exists():
            response = JsonResponse({'message' : 'You already liked this post'})
            return response
        else:
            post = Post.objects.get(id=post_id)
            post.favorited.add(request.user)
            post.save()
            response = JsonResponse({'times_liked': post.favorited.count()})
            return response

def comment(request):
    pass