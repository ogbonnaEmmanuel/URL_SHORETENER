from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('home')
        self.sign_up_url = reverse('sign_up')
        self.sign_in_url = reverse('sign_in')
        self.sign_out_url = reverse('sign_out')
        self.user_link_info_url = reverse('link_info')

    def test_home_view(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_sign_up_view(self):
        response = self.client.get(self.sign_up_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')

    def test_sign_in_view(self):
        response = self.client.get(self.sign_in_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_in.html')

    def test_sign_out_view(self):
        response = self.client.get(self.sign_out_url)
        self.assertEquals(response.status_code, 302)
