from django.test import TestCase, Client
from django.utils import timezone
from .models import MoodEntry
from django.contrib.auth.models import User


class MainTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='nagi', password='bluelock13') # create user
        self.client = Client()  # changed Client()
        self.client.login(username='nagi', password='bluelock13') 
        self.client.cookies['last_login'] = '2024-10-20T11:21:45' 

    def test_main_url_is_exist(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = self.client.get('/skibidi/')  # Non-existent URL
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        now = timezone.now()
        mood = MoodEntry.objects.create(
          user = self.user,
          mood="Happy",
          time = now,
          feelings = "I'm happy, even though my clothes are soaked from the rain :(",
          mood_intensity = 8,
        )
        self.assertTrue(mood.is_mood_strong)

    def test_main_template_uses_correct_page_title(self):
        response = self.client.get("/")
        html_response = response.content.decode("utf8")
        self.assertIn("PBD Mental Health Tracker", html_response)