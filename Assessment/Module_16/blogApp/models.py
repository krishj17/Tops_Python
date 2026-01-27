from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    createdAt = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("follower", "following")


class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    coverImage = models.ImageField(upload_to="coverImages", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    createdAt = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    createdAt = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("user", "post")

