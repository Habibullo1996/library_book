from django.contrib import admin

from books.models import Book


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']
    list_filter = ['title', 'author', 'price']
    search_fields = ['title', 'author']
