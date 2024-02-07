from rest_framework import serializers

from .models import Scientists


class ScientistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Scientists
        fields = ('full_name', 'degree', 'discription', 'birthday', 'diedday',)