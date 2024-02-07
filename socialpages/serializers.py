from rest_framework import serializers

from .models import SocialPages


class SocialPageSerializer(serializers.ModelSerializer):
    class Meta:
        model=SocialPages
        fields = ('instagram', 'telegram', 'facebook', 'address', 'phone', 'email',)