import os

from django.test import TestCase
from rest_framework.test import APIClient
from blog.models import BlogEntries
from django.contrib.auth.models import User
# Create your tests here.



class BasicTest(TestCase):

    def setUp(self):

        self.body = '''
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
        It has survived not only five centuries, but also the leap into electronic typesetting,
        remaining essentially unchanged.
        It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum
        passages, and more recently with desktop publishing software like Aldus PageMaker
        including versions of Lorem Ipsum. 
        '''

        self.client = APIClient()

        BlogEntries.objects.create(title="title 1", body=self.body, tags="tag1, tags2", published=True)
        BlogEntries.objects.create(title="title 2", body=self.body, tags="tag3, tags4", published=True)
        BlogEntries.objects.create(title="title 3", body=self.body, tags="tag5, tags6", published=False)


    def test_listing(self):
        entries = self.client.get('http://127.0.0.1:8000/api/articles/')
        self.assertEqual(entries.status_code, 200)
        self.assertEqual(len(entries.data), 2)

    def test_normal_user_cant_create_entry(self):
        data = {'title':'title 45', 'body':self.body, 'tags':'tag13, tags2', 'published':True}
        result = self.client.post('http://127.0.0.1:8000/api/article/create/', data=data)

        self.assertEqual(result.status_code, 403)




class AdminTest(TestCase):


    def setUp(self):

        self.body = '''
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
        It has survived not only five centuries, but also the leap into electronic typesetting,
        remaining essentially unchanged.
        It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum
        passages, and more recently with desktop publishing software like Aldus PageMaker
        including versions of Lorem Ipsum. 
        '''

        self.admin = APIClient()

        my_admin = User.objects.create_superuser('admin', 'email@test.com', 'password')
        self.admin.login(username='admin' , password='password')

        BlogEntries.objects.create(title="title 1", body=self.body, tags="tag1, tags2", published=True)
        BlogEntries.objects.create(title="title 2", body=self.body, tags="tag3, tags4", published=True)
        BlogEntries.objects.create(title="title 3", body=self.body, tags="tag5, tags6", published=False)



    def test_admin_can_post_new_entries(self):

        data =  {'title':'again title 45', 'body':self.body, 'tags':'tag13, tags2', 'published':True}
        result = self.admin.post('http://127.0.0.1:8000/api/article/create/', data=data,  format='json')
        print(result.content)
        self.assertEquals(result.status_code, 201)