from django.contrib import admin
from .models import Cue, Post, Review
from django_summernote.admin import SummernoteModelAdmin


class CueAdmin(admin.ModelAdmin):
    list_display = ("prompt", "date")


admin.site.register(Cue, CueAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")


admin.site.register(Post, PostAdmin)
