from rest_framework import serializers

class FrameXVideoSerializer(serializers.Serializer):
    name = serializers.CharField()
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    frames = serializers.IntegerField()
    url = serializers.CharField()
    frame_rate = serializers.ListField(child=serializers.IntegerField())
    first_frame = serializers.URLField()
    last_frame = serializers.URLField()
