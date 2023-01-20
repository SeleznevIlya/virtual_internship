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

    def create(self, validated_data):
        return PerevalAdded.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.beauty_title = validated_data.get('beauty_title', instance.beauty_title)
        instance.title = validated_data.get('title', instance.title)
        instance.other_title = validated_data.get('other_title', instance.other_title)
        instance.coord_id = validated_data.get('coord_id', instance.coord_id)
        instance.winter_level_id = validated_data.get('winter_level_id', instance.winter_level_id)
        instance.spring_level_id = validated_data.get('spring_level_id', instance.spring_level_id)
        instance.summer_level_id = validated_data.get('summer_level_id', instance.summer_level_id)
        instance.autumn_level_id = validated_data.get('autumn_level_id', instance.autumn_level_id)
        instance.status = validated_data.get('status', instance.status)
        instance.areas_id = validated_data.get('areas_id', instance.areas_id)

        instance.save()
        return instance