from django.test import TestCase
from whats_for_dinner.models import *
from django.core.urlresolvers import reverse
from django.conf import settings
import os
import populate


class ModelsTestCase(TestCase):

    def setUp(self):
	    Restaurant.objects.create(name="Testaurant", address="Ashton Ln, Glasgow G12 8QR", latitude=55.00, longitude=-4.00)
	    Food.objects.create(name="Food", restaurant=Restaurant.objects.get(name="Testaurant"), price=5.00)

    def test_models_working(self):
        restaurant = Restaurant.objects.get(name="Testaurant")
        food = Food.objects.get(name="Food")
        self.assertEqual(restaurant.address, "Ashton Ln, Glasgow G12 8QR")
        self.assertEqual(food.price, 5.00)


class ViewsTestCase(TestCase):

	def test_view_has_title(self):
		response = self.client.get(reverse('index'))
		self.assertIn('<title>', response.content.decode())
		self.assertIn('</title>', response.content.decode())

	def test_index_using_template(self):
		response = self.client.get(reverse('index'))
		self.assertTemplateUsed(response, 'whats_for_dinner/index.html')


	def test_static_image(self):
		response = self.client.get(reverse('index'))
		self.assertIn('img src="/static/images/Whats-for-Dinner.jpg'.lower(), response.content.decode().lower())

	def test_population_script(self):
		populate.populate()
		restaurant = Restaurant.objects.get(name='Chow')
		self.assertEquals(restaurant.address, '98 Byres Road, Glasgow, G12 8TB')

		food1 = Food.objects.get(name='Mushroom Curry')
		self.assertEquals(food1.vegetarian, True)

		food2 = Food.objects.get(name='Salmon Feast Set')
		self.assertEquals(food2.restaurant.name, 'Okome')

	def test_access_page(self):
		response = self.client.get(reverse('result'))
		self.assertEquals(response.status_code, 200)
		self.assertNotEquals(response.content.decode(), '')

	def test_base_template_exists(self):
		path_to_base = settings.TEMPLATE_DIR + '/whats_for_dinner/base.html'
		print(path_to_base)
		self.assertTrue(os.path.isfile(path_to_base))
