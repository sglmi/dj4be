from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.testuser = get_user_model().objects.create_user(
            username="testuser",
            email="test@mail.com",
            password="secreetpass"
        )
    
        self.post = Post.objects.create(
            title = "post title",
            body = "post body",
            author = self.testuser

        )
    
    def test_string_representation(self):
        post = Post(title="A sample tilte")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'post title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'post body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "post body")
        self.assertTemplateUsed(response, "home.html")
        
    def test_post_detail_view(self):
        response = self.client.get("/post/1/")
        no_response = self.client.get('/post/100000000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "post body")
        self.assertTemplateUsed(response, 'post_detail.html')
