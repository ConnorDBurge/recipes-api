from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = 'test@email.com'
        password = '12345'
        user = get_user_model().objects.create_user(
            email=email, password=password
            )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@EMAIL.COM'
        password = '12345'
        user = get_user_model().objects.create_user(
            email=email, password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None, password='12345'
            )

    def test_superuser_created(self):
        """Test creating a new user superuser"""
        email = 'test@email.com'
        password = '12345'
        user = get_user_model().objects.create_superuser(
            email=email, password=password
            )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
