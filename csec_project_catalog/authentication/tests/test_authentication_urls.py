from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Registration and Forget Password / Reset Password Urls Test
class RegistrTest(SimpleTestCase):

    def test_register_status(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_url_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_complete_url_name(self):
        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_complete_url_name(self):
        response = self.client.get(reverse('change_password_done'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_url_name(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_complete_url_name(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_complete_url_name(self):
        response = self.client.get(reverse('password_reset_confirm'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_complete_url_name(self):
        response = self.client.get(reverse('password_reset_complete'))
        self.assertEqual(response.status_code, 200)

# Login Urls Test
class LoginTest(SimpleTestCase):

    def test_login_url_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_url_name(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_befor_login_profile_url_name(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)



        
        
        
        
        
