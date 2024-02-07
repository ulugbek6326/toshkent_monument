from rest_framework import serializers

from .models import AboutForWe

class AboutForWeSerializer(serializers.ModelSerializer):
    class Meta:
        model=AboutForWe
        fields = ('img', 'description',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.aboutforme_images.all()
        print(images)

        if images:
            data['images'] = [{'image': img.image.url} for img in images]

        return data