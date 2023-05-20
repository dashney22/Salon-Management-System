from django.contrib import admin

from .models import Book

# Register your models here.
# Import model name (.[model_name] if they from the same folder!) admin.site.Register

admin.site.register(Book)

# Admin customisation
"""
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    #fields = ['','']---> shows which fields you want
    #list_display = ['',''] -- > what to be displayed
    #list_filter = ['published'] --> This feature allows you to filter records by date published
    """ 