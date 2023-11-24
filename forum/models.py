from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # images

STATUS = ((0, "Draft"), (1, "Published"))


class Cue(models.Model):
    prompt = models.CharField(max_length=45, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.prompt


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts")
    published = models.DateField(auto_now_add=True)
    edited_on = models.DateField(auto_now=True)
    content = models.TextField
    plot = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="post_likes", blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comment")
    posted_on = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=280)  # old twitter limit
    approve = models.BooleanField(default=False)

    def __str__(self):
        return f"Review {self.body} by {self.name} "
