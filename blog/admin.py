# coding: utf-8
# Register your models here.

from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    list_per_page = 5

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
