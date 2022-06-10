from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50, blank=True)
    avl = models.BooleanField(default=True)
    issued_to = models.PositiveIntegerField(default=0)

class BookIssue(models.Model):
    bookName = models.CharField(max_length=50, blank=True)
    reader_id = models.PositiveBigIntegerField()