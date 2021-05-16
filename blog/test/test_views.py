from django.test import TestCase, Client
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, resolve
from blog.models import Post, Author, User, Comment

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='password'
        )
        self.author = Author.objects.create(user=self.user)
        self.post1 = Post.objects.create(id=1, title='title', author=self.author, body='body of title')
        self.detail_url = reverse('post_detail', kwargs={'id': Post.objects.get().id})
        self.create_url = reverse('post_create')

    
    def test_home_view(self):
        response = self.client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')



    def test_post_create_view_GET(self):
        response = self.client.get(self.create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_create.html')


    def test_post_create_POST_adds_post(self):
        new_post = {'id': 2, 'author': self.author, 'title': 'new title', 'body': 'new body'}
        
        response = self.client.post(redirect(self.create_url), new_post)
        # print(resolve(response))
        p2 = Post.objects.all()
        p3 = Post.objects.get(id=2)
        print(p2)
        
            # print(p2.body)
        self.assertEquals(response.status_code, 200)
            # self.assertEquals(Post.objects.all().count(), 2)
            # self.assertEquals(Post.objects.get(id=2).title, 'test new title')
            # self.assertTemplateUsed(response, 'post_detail.html')
