from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'favorited')

    list_filter = ['published']

    search_fields = ['title']

admin.site.register(Post)