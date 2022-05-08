from django.contrib import admin
from .models import *

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

admin.site.register(TaskManager, ArticleAdmin)
admin.site.register(Comment)