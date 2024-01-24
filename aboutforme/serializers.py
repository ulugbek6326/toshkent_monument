from rest_framework import serializers

from .models import AboutForWe

class AboutForWeSerializer(serializers.ModelSerializer):
    class Meta:
        model=AboutForWe
        fields = '__all__'