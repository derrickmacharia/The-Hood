from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Test Location')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.save_location()
        self.location.delete()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)


class PostTestClass(TestCase):
    def setUp(self):
        self.post = Post(title='Test Post')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_method(self):
        self.post.save()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        self.post.save()
        self.post.delete_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 0)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.business = Business(name='Test Business')

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_method(self):
        self.business.save()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_method(self):
        self.business.save()
        self.business.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)