from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    desc = serializers.CharField()
    is_published = serializers.BooleanField()
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)
    # location = serializers.SerializerMethodField()

    # def get_location(self, obj):
    #     location='namakkal'
    #     return obj.location

    def create(self,validated_data):
        return Blog.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.desc = validated_data.get('desc',instance.desc)
        instance.is_published = validated_data.get('is_published',instance.is_published)
        instance.save()
        return instance
    
    