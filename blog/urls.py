from rest_framework import routers
from blog.views import ListEntriesView, EntryDetailsView, CreateEntryView, EntryDelete, EntryUpdate

from django.urls import path

router = routers.SimpleRouter()
#router.register(r'', ListEntriesView)


urlpatterns = [
     #url(r'', include((router.urls, 'blog_api'))),
     path('articles/', ListEntriesView.as_view()),
     path('article/create/', CreateEntryView.as_view()),
     path('article/<slug:slug>/', EntryDetailsView.as_view()),
     
     path('article/<slug:slug>/update', EntryUpdate.as_view()),
     path('article/<slug:slug>/delete', EntryDelete.as_view()),
     
]