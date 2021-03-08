from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created']


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ['posted_date']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
