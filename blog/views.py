from blog.models import BlogEntries
from blog.serializers import BlogEntriesSerializer

from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAdminUser 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.
#pagination_class
#filter_backends


#List all blog Posts
class ListEntriesView(generics.ListAPIView):
    
    serializer_class = BlogEntriesSerializer

    def get_queryset(self):
        return BlogEntries.objects.all().filter(published=True)

class CreateEntryView(mixins.CreateModelMixin, generics.GenericAPIView):
                  
    queryset = BlogEntries.objects.all()
    serializer_class = BlogEntriesSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#Blog details
class EntryDetailsView(generics.RetrieveAPIView):

    queryset = BlogEntries.objects.all()
    serializer_class = BlogEntriesSerializer
    
    lookup_field = 'slug'


#Delete
class EntryDelete(generics.DestroyAPIView):
    
    queryset = BlogEntries.objects.all()
    serializer_class = BlogEntriesSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    lookup_field = 'slug'


class EntryUpdate(generics.UpdateAPIView):

    queryset = BlogEntries.objects.all()
    serializer_class = BlogEntriesSerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    lookup_field = 'slug'