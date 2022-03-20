from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()
class BaseTest(TestCase):
	def setUp(self):
		self.register_url = reverse('register')
		self.login_url = reverse('login')
		self.user = get_user_model().objects.create_user(

			first_name = 'firstName',
			last_name = 'lastName',
			username = 'mrpguy',
			phone_number = '+25198765432',
			email = 'scott@users.com',
			password = 'x12344567x',

		)
		def test_user_instance(self):
			"""
			Check the user instance was created successfully
			"""
			self.assertIsInstance(self.user, User)
		self.userobj = {

			'first_name':'firstName',
			'last_name':'lastName',
			'username':'mrpguy1',
			'phone_number':'+12125552777',
			'email':'scott@users.com',
			'password':'x12344567x',

		}
		self.user_with_invalid_password = {

			'first_name':'firstName',
			'last_name':'lastName',
			'username':'mrpguy',
			'phone_number':'+25198765432',
			'email':'scott@users.com',
			'password':'',

		}
		self.user_with_invalid_email = {
		
			'first_name':'firstName',
			'last_name':'lastName',
			'username':'mrpguy',
			'phone_number':'+25198765432',
			'email':'testemail.gmailcom',
			'password':'12345',

		}
		return super().setUp()


# Registration and Forget Password / Reset Password View Test
class RegisterTest(BaseTest):

	def test_can_view_page_correctly(self):
		response = self.client.get(self.register_url)
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'authentication/register.html')

	def test_can_register_user(self):
		response = self.client.post(self.register_url, self.userobj, format = 'text/html')
		self.assertEqual(response.status_code,200)

	def test_can_not_register_user_with_invalid_password(self):
		response = self.client.post(self.register_url, self.user_with_invalid_password, format = 'text/html')
		self.assertEqual(response.status_code,200)

	def test_can_not_register_user_with_invalid_email(self):
		response = self.client.post(self.register_url, self.user_with_invalid_email, format = 'text/html')
		self.assertEqual(response.status_code,200)

	def test_can_not_register_users_with_similar_email(self):
		self.client.post(self.register_url, self.userobj, format = 'text/html')
		response = self.client.post(self.register_url, self.userobj, format = 'text/html')
		self.assertEqual(response.status_code,200)


# Login View Test
class LoginTest(BaseTest):

    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'registration/login.html')

    def test_login_success(self):
        self.client.post(self.register_url,self.userobj,format='text/html')
        user = get_user_model().objects.filter(email=self.userobj['email']).first()
        user.is_active = True
        user.save()
        response = self.client.post(self.login_url,self.userobj,format = 'text/html')
        self.assertEqual(response.status_code,200)

    def test_can_view_profile_page_with_login_success(self):
        self.client.post(self.register_url,self.userobj,format='text/html')
        user = get_user_model().objects.filter(email=self.userobj['email']).first()
        user.is_active = True
        user.save()
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code,302)

    def test_can_not_login_with_no_username(self):
        response= self.client.post(self.login_url,{'password':'passwped','username': ''},format='text/html')
        self.assertEqual(response.status_code,200)

    def test_can_not_login_with_no_password(self):
        response= self.client.post(self.login_url,{'username':'passwped','password':''},format='text/html')
        self.assertEqual(response.status_code,200)
	
	
	
	
	
	
