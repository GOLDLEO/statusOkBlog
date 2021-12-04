from django.contrib import admin
from .models import Post, Tag
from .models import Post, Tag, Comment

admin.site.register(Post)
admin.site.register(Tag)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('user_name', 'email', 'comment_text')


admin.site.register(Comment, CommentAdmin)
