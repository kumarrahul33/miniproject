from django.contrib import admin
from .models import BookIssue, Book

admin.site.register(Book)
admin.site.register(BookIssue)

# Register your models here.
