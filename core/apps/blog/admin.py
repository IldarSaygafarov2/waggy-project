from django.contrib import admin

from .models import BlogPost, BlogPostTag

@admin.register(BlogPostTag)
class BlogPostTagAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    