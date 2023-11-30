from django.contrib import admin
from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'is_published')
    list_display_links = ('id', 'title', 'desc')
    list_editable = ('is_published',)
    search_fields = ('title', 'desc')
    list_per_page = 1
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'desc',
                'is_published'
            ),
        }),
    )
    ordering = ['id']

admin.site.register(Blog, BlogAdmin)
    