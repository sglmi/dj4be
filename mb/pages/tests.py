from django.test import TestCase
from django.urls import reverse

from .models import Post


# class PostModelTest(TestCase):
#     def setup(self):
#         Post.objects.create(text="just a test")

#     def test_text_content(self):
#         post = Post.objects.get(id=1)
#         expected_object_name = f"{post.text}"
#         self.assertEqual(expected_object_name, "just a test")


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="just a test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.text}"
        self.assertEqual(expected_object_name, "just a test")


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Some text")

    def test_view_url_exsit_at_proper_url(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_by_url_name(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")
