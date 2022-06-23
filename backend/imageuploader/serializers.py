from rest_framework import serializers
from imageuploader.models import Image

class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'