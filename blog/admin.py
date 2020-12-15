from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display=['title', 'author', 'date']
	list_filter = ['date', 'author']
	search_fields = ['title']

admin.site.register(Post, PostAdmin)