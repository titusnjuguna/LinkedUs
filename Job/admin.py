from django.contrib import admin
from .models import Jobs,Candidates


@admin.register(Jobs)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'experience', 'salary', 'location','published')
    list_filter = ('salary', 'location', 'published')
    search_field = ('title', 'experience')
    ordering = ('published',)



