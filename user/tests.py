from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import User
# Create your tests here.

class TUserTests(TestCase):
  def setUp(self):
    return super().setUp()
  def test_using_custom_user(self):
    self.assertEqual(get_user_model(),User)
