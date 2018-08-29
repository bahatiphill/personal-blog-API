from django.shortcuts import render
from blog.models import BlogEntries
from blog.serializers import BlogEntriesSerializer

from rest_framework import mixins
from rest_framework import generics



# Create your views here.



class BlogEntriesList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = BlogEntries.objects.all()
    serializer_class = BlogEntriesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)





class BlogEntryDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = BlogEntries.objects.all()
    serializer_class = BlogEntriesSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)