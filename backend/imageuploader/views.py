from rest_framework import viewsets
from imageuploader.models import Image
from imageuploader.serializers import ImageModelSerializer

# Create your views here.
class ImageModelViewSet(viewsets.ModelViewSet):
    serializer_class = ImageModelSerializer
    queryset = Image.objects.all()