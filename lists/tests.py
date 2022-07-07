from urllib import response
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
        
    