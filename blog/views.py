from blog.models import BlogEntries
from blog.serializers import BlogEntriesSerializer

from rest_framework import mixins
from rest_framework import generics



# Create your views here.
#pagination_class
#filter_backends

'''
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

'''



#List all blog Posts
class ListEntriesView(generics.ListAPIView):
    
    queryset = BlogEntries.objects.all()
    serializer_class = BlogEntriesSerializer


class CreateEntryView(mixins.CreateModelMixin, generics.GenericAPIView):
                  
    queryset = BlogEntries.objects.all()
    serializer_class = BlogEntriesSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#Blog details
class EntryDetailsView(generics.RetrieveAPIView):

    queryset = BlogEntries.objects.all()
    serializer_class = BlogEntriesSerializer
    
    lookup_field = 'slug'
