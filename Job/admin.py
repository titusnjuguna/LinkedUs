from django.contrib import admin
from .models import Jobs,Candidates


@admin.register(Jobs)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'experience', 'slug','salary','location','publish')
    list_filter = ('salary', 'location', 'publish')
    search_field = ('title', 'experience')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('publish',)


@admin.register(Candidates)
class Candidates(admin.ModelAdmin):
    list_display = ('name', 'dob', 'gender', 'mobile', 'email', 'resume')
    list_filter = ('name', 'gender', 'email')
