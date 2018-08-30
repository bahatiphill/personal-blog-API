from rest_framework import serializers
from blog.models import BlogEntries




class BlogEntriesSerializer(serializers.ModelSerializer):

    slug = serializers.PrimaryKeyRelatedField(read_only=True, default='--'

    class Meta:
        model = BlogEntries
        fields = ('id','title','body', 'tags')
        read_only_fields = ('slug',)