from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # images

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    posted_on = models.DateField(auto_now_add=True)
    edited_on = models.DateField(auto_now=True)
    content = models.TextField
    preview = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="forum_likes", blank=True)
