from rest_framework import routers
from blog.views import BlogEntryDetail, BlogEntriesList

from django.conf.urls import  include

router = routers.SimpleRouter()
router.register(r'blog', BlogEntriesList)


urlpatterns = [
     url(r'^api/', include((router.urls, 'blog_api'))),
]