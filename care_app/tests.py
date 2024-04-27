from django.test import TestCase
from django.urls import reverse
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By

from .models import CustomUser, Patient
from .forms import UserRegisterForm


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser', email='test@example.com', role='admin')

    def test_user_string_representation(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.role, 'admin')

    def test_user_email(self):
        user = CustomUser.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')


class FormTestCase(TestCase):
    def test_user_register_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'passwordToTest',
            'password2': 'passwordToTest',
            'role': 'admin'
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

class ViewTestCase(TestCase):

    def test_user_login_view(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_logout_view(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class IntegrationTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_user_registration(self):
        # Go to registration page
        self.selenium.get(self.live_server_url + '/register/')

        # Find the username input and input testuser
        username_input = self.selenium.find_element(By.NAME, 'username')
        username_input.send_keys('testuser')

    def test_user_login(self):
        # Go to login page
        self.selenium.get(self.live_server_url + '/login/')

        # Find the username and password inputs and fill them
        username_input = self.selenium.find_element(By.NAME, 'username')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('testuser')
        password_input.send_keys('password123')

        # Submit the form
        self.selenium.find_element(By.XPATH, "//button[text()='Login']").click()

    def test_user_logout(self):
        # Log in first
        self.selenium.get(self.live_server_url + '/login/')
        username_input = self.selenium.find_element(By.NAME, 'username')
        password_input = self.selenium.find_element(By.NAME, 'password')
        username_input.send_keys('testuser')
        password_input.send_keys('password123')
        self.selenium.find_element(By.XPATH, "//button[text()='Login']").click()

        # Go to logout page
        self.selenium.get(self.live_server_url + '/logout/')

    def test_update_patient_name(self):
        # Create a patient object
        patient = Patient.objects.create(name='Test Patient', email='test@example.com', phone='1234567890',
                                         dob='2000-01-01')

        # Go to the patient detail page
        self.selenium.get(self.live_server_url + f'/patient/{patient.id}/')

        # Find the edit button and click it
        edit_button = self.selenium.find_element(By.XPATH, "//i[contains(@class, 'bi-pencil')]")
        edit_button.click()

        # Find the input field for updating the name and fill it
        name_input = self.selenium.find_element(By.NAME, 'name')
        name_input.clear()
        name_input.send_keys('Updated Name')

        # Find the save button and click it
        save_button = self.selenium.find_element(By.XPATH, "//button[text()='Update Information']")
        save_button.click()

        # Check if the patient's name is updated
        updated_patient = Patient.objects.get(id=patient.id)
        self.assertEqual(updated_patient.name, 'Updated Name')
