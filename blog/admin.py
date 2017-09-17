from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    exclude = ['favorited', 'comments']

    list_display = ('title', 'published')

    list_filter = ['published']

    search_fields = ['title']

admin.site.register(Post, PostAdmin)