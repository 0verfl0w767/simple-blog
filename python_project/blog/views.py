from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Post, Comment

def post(request):
  return render(request, "post.html", { "posts": Post.objects.all().order_by("-id") })

def post_create(request):
  if "id" not in request.session:
    return redirect("/")
  if request.method == "GET":
    return render(request, "post_create.html")
  if request.method == "POST":
    data = {
      "uid": request.session["id"],
      "title": request.POST["title"],
      "content":request.POST["content"],
    }
    if "thumbnail" in request.FILES:
      data["thumbnail"] = request.FILES["thumbnail"]
    post = Post.objects.create(**data)
    return redirect(f"/posts/read/{post.id}")

def post_read(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.method == "POST":
    Comment.objects.create(
      uid=request.session["id"],
      post=post,
      content=request.POST["comment"],
    )
  return render(request, "post_read.html", { "post": post })

def post_update(request, post_id):
  if "id" not in request.session:
    return redirect("/")
  post = Post.objects.get(id=post_id)
  if request.session["id"] != post.uid:
    return HttpResponse("<script>alert(\"자신이 쓴 글이 아닙니다.\"); location.href=\"/\";</script>")
  if request.method == "GET":
    return render(request, "post_update.html", { "post": post })
  if request.method == "POST":
    post.title = request.POST["title"]
    post.content = request.POST["content"]
    if "thumbnail" in request.FILES:
      post.thumbnail = request.FILES["thumbnail"]
    post.save()
    return HttpResponse("<script>alert(\"수정 되었습니다.\"); location.href=\"/posts/\";</script>")

def post_delete(request, post_id):
  if "id" not in request.session:
    return redirect("/")
  post = Post.objects.get(id=post_id)
  if request.session["id"] != post.uid:
    return HttpResponse("<script>alert(\"자신이 쓴 글이 아닙니다.\"); location.href=\"/\";</script>")
  post.delete()
  return HttpResponse("<script>alert(\"삭제 되었습니다.\"); location.href=\"/posts/\";</script>")