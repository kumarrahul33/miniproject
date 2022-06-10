#from dataclasses import fields
from rest_framework import serializers
from bookissue.models import Book, BookIssue
from libmembership.models import member

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = member
        fields = '__all__'

class BookIssueSerialiaer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = '__all__'
