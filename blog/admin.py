from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_on",)
    filter_horizontal = ("authors", )

# admin.site.register(BlogPost, BlogPostAdmin)
