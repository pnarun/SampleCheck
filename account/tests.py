from django.test import TestCase

from . import views

# Create your tests here.

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
    
    def test_home_page_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Homepage</h1>')
    
    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi there! I should not be on this page.')
    
    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'testpage.html')
    
    