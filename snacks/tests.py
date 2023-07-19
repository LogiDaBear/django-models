from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from snacks.models import Snacks

class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester', email='tester@email.com', password='pass')
        self.snack = Snacks.objects.create(
            name='snack1', rating=10, purchaser=self.user)
        
    def test_string_representation(self):
        self.assertEqual(str(self.snack), 'snack1')

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')
        
