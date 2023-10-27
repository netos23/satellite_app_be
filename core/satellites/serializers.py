from rest_framework import serializers
from pictures.serializers import PictureSerializer


class SatteliteSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField(source='object_name')
    picture = serializers.URLField()
    resolution = serializers.FloatField()
