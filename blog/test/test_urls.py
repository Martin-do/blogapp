from django.test import TestCase, Client
# from blog.models import Post, Author, User
from django.utils import timezone
from django.urls import reverse, resolve
from blog.models import Post, User, Author
from blog.views import home, post_detail, create_post, post_edit, post_delete

# Create your tests here.

# url test
class URL_test(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='password'
        )
        self.author = Author.objects.create(user=self.user)
        self.post1 = Post.objects.create(id=1, title='title', author=self.author, body='body of title', timestamp=timezone.now())


    def test_home_url_is_resolve(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
    
    def test_create_post_url_is_resolve(self):
        url = reverse('post_create')
        self.assertEquals(resolve(url).func, create_post)

    def test_post_detail_url_is_resolve(self):
        post_id = self.post1.id
        url = reverse('post_detail', kwargs={ 'id': post_id})
        self.assertEquals(resolve(url).func, post_detail)

    def test_post_edit_url_is_resolve(self):
        post_id = self.post1.id
        url = reverse('post_edit', kwargs={ 'id': post_id})
        self.assertEquals(resolve(url).func, post_edit)

    def test_post_delete_url_is_resolve(self):
        post_id = self.post1.id
        url = reverse('post_delete', kwargs={ 'id': post_id})
        self.assertEquals(resolve(url).func, post_delete)


    # def user(self):
    #     self.user = User.objects.create_user(
    #         username='test',
    #         email='test@gmail.com',
    #         password='password'
    #     )
    #     self.author = Author.objects.create(user=self.user)
    #     return self.author

    #     self.post = Post.objects.create(title='title', author=self.author, body='body of title', timestamp=timezone.now())
    #     return self.post
    #     print(self.post)

    # def test_string_representation(self):
    #     post = Post(title='A simple title')
    #     self.assertEqual(str(post), post.title)


    # def test_post_content(self):
    #     self.assertEqual(f'{self.post.title}', 'title')
    #     self.assertEqual(f'{self.post.author}', 'testauthor')
    #     self.assertEqual(f'{self.post.body}', 'body of title')

    # def test_post_creation(self):
    #     p = self.user()
    #     self.assertTrue(isinstance(p, Post))

    # def test_post_list_view(self):
    #     response = self.client.get(reverse('none'))
    #     self.assertEqual(response.status_code, 200),
    #     self.assertContains(response, 'nice body')
    #     self.assertTemplateUsed(response, 'home.html')

    # def test_post_detail_view(self):
    #     response = self.client.get('/post/1/')
    #     no_response = self.client.get('/post/500/')
    #     self.assertEqual(response.status_code, 200),
    #     self.assertEqual(no_response.status_code, 404),
    #     self.assertContains(response, 'nice body')
    #     self.assertTemplateUsed(response, 'post_detail.html')