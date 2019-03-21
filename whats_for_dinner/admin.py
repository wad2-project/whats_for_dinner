from django.contrib import admin
from whats_for_dinner.models import *


class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('name', 'image', 'address', 'latitude', 'longitude')


class FoodAdmin(admin.ModelAdmin):
	list_display = ('name', 'restaurant', 'price', 'vegetarian', 'description')


class UserFavouritesAdmin(admin.ModelAdmin):
	list_display = ('user',)


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(UserFavourites, UserFavouritesAdmin)
