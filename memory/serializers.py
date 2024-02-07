from rest_framework import serializers

from .models import Memory


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ('title', 'img', 'description', 'like', 'video', 'longitude', 'latitude',)