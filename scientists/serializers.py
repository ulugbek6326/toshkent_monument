from rest_framework import serializers

from .models import Scientists


class ScientistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Scientists
        fields='__all__'