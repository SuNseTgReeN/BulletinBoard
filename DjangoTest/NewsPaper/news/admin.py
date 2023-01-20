from django.contrib import admin
from .models import Author, Category, Post, Comment, PostCategory


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_creation', 'category_type', 'post_author', 'rating')
    list_filter = ('date_creation', 'category_type', 'post_author', 'rating')
    search_fields = ('title', 'category_type')


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(PostCategory)
