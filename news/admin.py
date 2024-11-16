from django.contrib import admin
from.models import *

class NewAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'discription']
    list_display_links = ['title']
    search_fields = ['title']


admin.site.register(News, NewAdmin)