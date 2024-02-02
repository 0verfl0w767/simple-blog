from django.shortcuts import render, redirect
from blog.models import Post, Comment

def post(request):
  posts = Post.objects.all().order_by("-id")
  context = {
    "posts": posts,
  }
  return render(request, "post.html", context)

def post_create(request):
  if request.method == "POST":
    title = request.POST["title"]
    content = request.POST["content"]
    if "thumbnail" in request.FILES:
      post = Post.objects.create(
        title=title,
        content=content,
        thumbnail=request.FILES["thumbnail"],
      )
    else:
      post = Post.objects.create(
        title=title,
        content=content,
      )
    return redirect(f"/posts/read/{post.id}")
  else:
    return render(request, "post_create.html")

def post_read(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.method == "POST":
    comment_content = request.POST["comment"]
    Comment.objects.create(
      post=post,
      content=comment_content,
    )
  context = {
    "post": post,
  }
  return render(request, "post_read.html", context)

def post_update(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.method == "POST":
    title = request.POST["title"]
    content = request.POST["content"]
    post.title = title
    post.content = content
    if "thumbnail" in request.FILES:
      post.thumbnail = request.FILES["thumbnail"]
    post.save()
    return redirect(f"/posts/read/{post.id}")
  else:
    context = {
      "post": post,
    }
    return render(request, "post_update.html", context)

def post_delete(request, post_id):
  post = Post.objects.get(id=post_id)
  post.delete()
  return redirect(f"/posts/")