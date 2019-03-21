from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
	name = models.CharField(max_length=64)
	image = models.ImageField()
	address = models.CharField(max_length=64)
	latitude = models.DecimalField(decimal_places=6, max_digits=9)
	longitude = models.DecimalField(decimal_places=6, max_digits=9)

	def __str__(self):
		return self.name


class Food(models.Model):
	name = models.CharField(max_length=64)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	price = models.DecimalField(decimal_places=2, max_digits=4)
	vegetarian = models.BooleanField(default=False)
	description = models.CharField(max_length=32)

	def __str__(self):
		return self.name


class UserFavourites(models.Model):
	user = models.OneToOneField(User)
	favourites = models.ManyToManyField(Food)

	class Meta:
		verbose_name_plural = 'UserFavourites'

	def __str__(self):
		return self.user.username
