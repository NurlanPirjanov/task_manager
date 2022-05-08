from django.contrib import admin
from .models import *

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]
    list_display = ['title','author','ot_date','do_date','role_user',]
admin.site.register(TaskManager, ArticleAdmin)
admin.site.register(Comment)