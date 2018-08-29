from rest_framework import serializers
from blog.models import BlogEntries




class BlogEntriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogEntries
        fields = '__all__'