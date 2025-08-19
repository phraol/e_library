from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'uploaded_by', 'created_at')
    search_fields = ('title', 'author')
