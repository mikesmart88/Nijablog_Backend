from rest_framework import serializers
from .models import Article
from .utils import calculate_read_time


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username')
    file_url = serializers.CharField(source='post_file.file_url')
    file_type = serializers.CharField(source='post_file.type')
    location = serializers.CharField(source='region.name')
    read_time = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'cartegory', 'content', 'tags', 'author_name', 'created_at', 'post_uuid', 'file_url', 'location',
                  'read_time', 'reads', 'file_type' ]
        
    def get_read_time(self, obj):
            return calculate_read_time(obj.content)
        
    def get_tags(self, obj):
        return list(obj.tags.values_list('name', flat=True))