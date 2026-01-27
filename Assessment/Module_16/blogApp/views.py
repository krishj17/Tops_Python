from django.shortcuts import render, redirect
from django.http import JsonResponse
from blogApp.models import *
from django.utils.text import slugify
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



# PAGE VIEWS:
def home_page(request):
    return render(request, "home_page.html")

@login_required(login_url="login")
def dashboard_page(request):
    user = User.objects.get(username="admin")
    categories = Category.objects.all()
    data = Post.objects.filter(user=user)
    print(data)
    return render(request, "dashboard_page.html", {"userBlogs":data, "categories": categories})

def blogs_page(request):
    post_list = Post.objects.all().order_by("-createdAt")
    paginator = Paginator(post_list, 6)
    print(paginator)
    page_number = request.GET.get("page") or 1
    posts = paginator.get_page(page_number)
    print(posts)
    return render(request, "blog_list_page.html", {"blogs":posts})

def blog_page(request, slug):
    post = Post.objects.get(slug=slug)
    all_post_likes = Like.objects.filter(post = post.id)  # find all likes of that post

    like_count = all_post_likes.count()
    user_has_like = False
    if request.user.is_authenticated:
        user_has_like = all_post_likes.filter(user = request.user.id).exists()

    print("has liked: ", user_has_like)

    all_comments = Comment.objects.filter(post=post.id).select_related("user").order_by("-createdAt")
    comments_data = []
    user_has_commented = False
    
    for c in all_comments:
        if c.user.id==request.user.id: 
            user_has_commented=True
        comments_data.append(
            {
                "id": c.id,
                "comment": c.comment,
                "createdAt": c.createdAt.strftime("%Y-%m-%d %H:%M"),
                "user": {
                    "id": c.user.id,
                    "username": c.user.username,
                }
            }
        )
        
    return render(request, "blog_page.html", {"post":post, "user_has_like":user_has_like, "like_count":like_count, "comments":comments_data, "user_has_commented": user_has_commented})

def register_page(request):
    return render(request, "register_page.html")

def login_page(request):
    return render(request, "login_page.html")

# dashboard - posts route handlers:
@login_required(login_url="login")
def get_posts(request):
    user = User.objects.get(username="admin")
    categories = Category.objects.all()
    data = Post.objects.filter(user=user)
    return JsonResponse({"status": "success", "userBlogs":data, "categories": categories})

@login_required(login_url="login")
def add_post(request):
    try:
        data = request.POST
        user = User.objects.get(username="admin") # afterwards replace this with actual user that we get from 'request.user'
        title = data["title"]
        categoryId = data["category"]
        body = data["body"]
        slug = slugify(title)
        coverImage = request.FILES.get("coverImage")
    
        pobj = Post(
            title = title,
            slug = slug,
            body = body,
            coverImage = coverImage,
            category = Category.objects.get(id=categoryId),
            user = user
        )
        pobj.save()
        return JsonResponse({"status":"success", "message":"Post added successfully!"})
    except Exception:
        print(Exception)
        return JsonResponse({"status":"error", "error":Exception})

@login_required(login_url="login")
def update_post(request):
    try:
        data = request.POST
        id = data["id"]
        title = data["title"]
        categoryId = data["category"]
        body = data["body"]
        slug = slugify(title)
        newCoverImage = request.FILES.get("coverImage")
        
        post = Post.objects.get(id=id)
        post.title=title
        post.category=Category.objects.get(id=categoryId)
        post.body=body
        post.slug=slug
        if newCoverImage:
            if post.coverImage:
                oldImg = post.coverImage  
                if os.path.isfile(f"./media/{oldImg}"):  # if old image exist remove it.
                    os.remove(f"./media/{oldImg}")
            post.coverImage = newCoverImage
        post.save()
            
        return JsonResponse({"status":"success", "message":"Post added successfully!"})
    except Exception:
        print(Exception)
        return JsonResponse({"status":"error", "error":Exception})

@login_required(login_url="login")   
def delete_post(request):
    data = request.POST
    id = data["id"]
    post = Post.objects.get(id=id)
    post.delete()
    return JsonResponse({"status": "success", "message": "post deleted successfully!"})

# blog page - like and comment handlers:
@login_required(login_url="login")
def like_post(request):
    try:
        data = request.POST
        postId = data["postId"]
    
        user_like = Like.objects.filter(post=postId, user=request.user.id)
        print(user_like)

        if user_like.exists():
            user_like.delete()
            return JsonResponse({"status": "success", "operation":"delete", "message": "Like added successfully!"})
        else:
            like = Like(
                user = request.user,
                post = Post.objects.get(id=postId),
            )
            like.save()
            return JsonResponse({"status": "success", "operation":"add", "message": "Like deleted successfully!"})

    except Exception:
        print(Exception) 
        return JsonResponse({"status": "error", "message":"Error while operating Like"})

@login_required(login_url="login")
def post_comment(request):
    try:
        data = request.POST
        postId = data["postId"]
        comment = data["comment"]
        
        com = Comment(
            comment = comment,
            user = request.user,
            post = Post.objects.get(id=postId)
        )
        com.save()
        
        # Get all comments related to this post, sort it and get the username.
        all_comments = Comment.objects.filter(post=postId).select_related("user").order_by("-createdAt")
        comments_data = []
        for c in all_comments:
            comments_data.append(
                {
                    "id": c.id,
                    "comment": c.comment,
                    "createdAt": c.createdAt.strftime("%Y-%m-%d %H:%M"),
                    "user": {
                        "id": c.user.id,
                        "username": c.user.username,
                    }
                }
            )
        return JsonResponse({"status":"success", "comments":comments_data, "message":"comment added successfully!"})
    
    except Exception:
        print(Exception)
        return JsonResponse({"status":"error", "error":"Error while operating comment!"})
    

# Register page:
def register_user(request):
    data = request.POST
    username = data["username"]
    email = data["email"]
    password = data["password"]
    role = data["role"]

    print(username, email, password, role)
    does_user_exist = User.objects.filter(username=username, email=email)
    if does_user_exist:
        return JsonResponse({"status":"error", "error":"Provided Email/User Already Exist."})
    
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    new_user.save()

    if role=="author":
        author_group = Group.objects.get(name="Author")
        new_user.groups.add(author_group)
    else :
        reader_group = Group.objects.get(name="Reader")
        new_user.groups.add(reader_group)
    
    return JsonResponse({"status":"success", "message":"user created successfully"})

def login_user(request):
    data = request.POST
    username = data["username"]
    password = data["password"]

    print(username, password)
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({"status":"success", "message":"user login successful!"})
    else:
        return JsonResponse({"status":"error", "message":"user does not exist. please provide valid credentials!"})

def logout_user(request):
    if request.user:
        logout(request)
        return redirect(home_page)