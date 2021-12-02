from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'pk',
            'title',
            'content',
            'meta_keywords',
            'meta_description',
            'date_create',
            'is_active',
            'count_view',
            'tag_name',
        )