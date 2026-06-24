from django.contrib import admin
from .models import Author, Publisher, Book, BookInstance

class BookAdmin(admin.ModelAdmin):

    fieldsets = [
        ('ISBN', {'fields': ['isbn']}),
        ('Title', {'fields': ['title']}),
        ('Author ID', {'fields': ['author_id']}),
        ('Publisher ID', {'fields': ['publisher_id']}),
        ('Publication Date', {'fields': ['year_pub']}),
        ('Description', {'fields': ['description']}),
    ]
    list_display = ('title', 'year_pub', 'description')
    list_filter = ['title','year_pub']

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(BookInstance)
