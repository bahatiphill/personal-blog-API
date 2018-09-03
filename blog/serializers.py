from rest_framework import serializers
from blog.models import BlogEntries




class BlogEntriesSerializer(serializers.ModelSerializer):

    slug = serializers.SlugField(read_only=True)
    timestamp = serializers.DateField(read_only=True)

    class Meta:
        model = BlogEntries
        fields = ('id','title','body', 'tags', 'slug', 'published', 'timestamp')
        #read_only_fields = ('slug',)
