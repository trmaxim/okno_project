from django.contrib import admin
from .models import Images

class PortfolioAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'pub_date')

admin.site.register(Images, PortfolioAdmin)

