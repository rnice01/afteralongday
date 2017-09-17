from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Post, Comment
# Create your views here.

def index(request):
    post = Post.objects.latest('published')
    return render(request, 'blogs.html', {'post': post})

def get_blog(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blogs.html', {'post': post})

def like_comment(request):
    if request.is_ajax():
        post_id = request.POST.get('post_id')
        if Post.objects.filter(id=post_id, favorited=request.user).exists():
            response = JsonResponse({'message' : 'You already liked this post'}, status=200)
            return response
        else:
            post = Post.objects.get(id=post_id)
            post.favorited.add(request.user)
            post.save()
            response = JsonResponse({'times_liked': post.favorited.count()}, status=200)
            return response

def comment(request):
    if request.is_ajax():
        post_id = request.POST.get('post_id')
        comment_text = request.POST.get('comment')
        user = request.user
        comment = Comment(user=user, text=comment_text)
        comment.save()
        post = Post.objects.get(id=post_id)
        post.comments.add(comment)
        post.save()
        response = JsonResponse({'comment_text': comment.text, 'comment_user': comment.user.username, 'comment_date': comment.date_posted}, status=200)
        return response

def edit_comment(request, comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        if request.user == comment.user:
            comment.text = request.POST.get('comment_text')
            comment.save()
            post = Post.objects.filter(comments=comment).first()
            return redirect('/blog/' + str(post.pk))

    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.user:
        return render(request, 'comment_form.html', {'comment': comment})
    else:
        return redirect('/blog')


def delete_comment(request):
    if request.is_ajax and request.method == "POST":
        comment = Comment.objects.get(id=request.POST.get('comment_id'))
        comment.delete()
        response = JsonResponse({'message': 'deleted comment'}, status=200)
        return response