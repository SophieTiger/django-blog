from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About, CollaborateRequest

class TestAboutViews(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.content = About(
            title="About title", content="About content")
        self.content.save()

    def test_render_about_page_with_collaboration_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse(
            'about'))
        print(response.context)            
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIn(b"About content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)


    def test_successful_collaboration_request_submission(self):
        """Test for posting a collaboration request"""
        post_data = {
            'name': 'Firstname Lastname',
            'email': 'email@test.com',
            'message': 'The message entered'
        }
        response = self.client.post(reverse(
            'about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )