from rest_framework import serializers
from .models import PerevalAdded


class PerevalSerializer(serializers.Serializer):

    author_id = serializers.IntegerField()
    beauty_title = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    other_title = serializers.CharField(max_length=255)
    connect = serializers.BooleanField(default=True)
    add_time = serializers.DateTimeField(read_only=True)
    coord_id = serializers.IntegerField()
    winter_level_id = serializers.IntegerField()
    spring_level_id = serializers.IntegerField()
    summer_level_id = serializers.IntegerField()
    autumn_level_id = serializers.IntegerField()
    status = serializers.CharField(read_only=True)
    areas_id = serializers.IntegerField()
    #activities_types = serializers.IntegerField()