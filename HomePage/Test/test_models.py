import secrets

from django.contrib.auth.models import User
from django.test import TestCase

from HomePage.models import Link


class TestModels(TestCase):
    def setUp(self):
        self.test_url = 'http://127.0.0.1:8000/add/'
        self.username = secrets.token_hex(10)
        self.password = secrets.token_hex(8)
        self.email = f'{secrets.token_hex(5)}@email.com'
        self.creator = User.objects.create(
            username='the_guy',
            email='eogbonna45@gmail.com',
            password='magmus345correct'
        )
        self.link = Link.objects.create(
            url='http://127.0.0.1:8000/add/',
            creator=self.creator,
            alias='add_web'
        )

    def test_is_link_and_user_created(self):
        link_obj = Link.objects.filter(creator=self.creator).first()
        user = User.objects.filter(username='the_guy').first()
        self.assertEquals(link_obj.creator.username, user.username)

    def test_is_link_active(self):
        link = Link.objects.filter(alias='add_web').first()
        self.assertFalse(link.is_link_active())

    def test_get_visitors(self):
        link = Link.objects.filter(alias='add_web').first()
        self.assertEquals(link.get_visitors(), 0)

    def test_link_created_for_annonymous_user(self):
        user = User.objects.create(
            username=self.username,
            password=self.password,
            email=self.email
        )
        link = Link.objects.create(
            url=self.test_url,
            alias='unknown_url',
            creator=user
        )
        created_link = Link.objects.filter(alias='unknown_url').first()
        self.assertEquals(created_link.alias, 'unknown_url')
