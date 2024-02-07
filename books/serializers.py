from rest_framework import serializers

from .models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('name', 'book_file',)