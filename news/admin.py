from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'published_date', 'author')
	prepopulated_fields = {"slug": ("title",)}





admin.site.register(News, NewsAdmin)

