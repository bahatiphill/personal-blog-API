from rest_framework import routers
from blog.views import ListEntriesView, EntryDetailsView, CreateEntryView

from django.urls import path

router = routers.SimpleRouter()
#router.register(r'', ListEntriesView)


urlpatterns = [
     #url(r'', include((router.urls, 'blog_api'))),
     path('articles/', ListEntriesView.as_view()),
     path('article/create/', CreateEntryView.as_view()),
     path('article/<slug:slug>/', EntryDetailsView.as_view()),
     
     #path('article/<slug:slug>/update'),
     #path('article/<slug:slug>/delete'),
     
]