from django.contrib.auth.views import LoginView
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from HomePage.views import home, sign_out


class TestUrls(SimpleTestCase):
    def test_home_page(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_sign_up_page(self):
        auth_url = reverse('sign_out')
        self.assertEquals(resolve(auth_url).func, sign_out)

    def test_sign_out_page(self):
        auth_url = reverse('sign_out')
        self.assertEquals(resolve(auth_url).func, sign_out)

    def test_sign_in_page(self):
        auth_url = reverse('sign_in')
        self.assertEquals(resolve(auth_url).func.view_class, LoginView)
