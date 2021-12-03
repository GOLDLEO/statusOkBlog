from rest_framework import serializers
from .models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'pk',
            'name',
        )


class PostSerializer(serializers.ModelSerializer):
    tag_name = TagSerializer(many=True)

    class Meta:
        model = Post
        # fields = "__all__"
        fields = (
            'pk',
            'title',
            'content',
            'meta_keywords',
            'meta_description',
            'date_create',
            'is_active',
            'count_view',
            'tag_name'
        )

