from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import  HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from whats_for_dinner.models import *
from whats_for_dinner.forms import *
import googlemaps
import random


def index(request):
	return render(request, 'whats_for_dinner/index.html')


def about(request):
	return render(request, 'whats_for_dinner/about.html')


def result(request):
	if request.method == 'POST':
		try:
			restaurants = get_restaurants(request.POST.get('postcode'))
			# Get food from favourites or all foods
			if request.POST.get('range') == 'favourites':
				favourites = UserFavourites.objects.filter(user=request.user)
				foods = list(favourites)[0].favourites.all()
				for favourite in favourites:
					foods.union(favourite.favourites.all())
			else:
				foods = Food.objects.all()
			foods = foods.filter(restaurant__in=restaurants) # Filter foods by nearby restaurants
			# Further filter foods by price and diet
			if request.POST.get('price_low') != 'low':
				foods = foods.exclude(price__lt=6)
			if request.POST.get('price_mid') != 'mid':
				foods = foods.exclude(price__gte=6, price__lt=10)
			if request.POST.get('price_high') != 'high':
				foods = foods.exclude(price__gte=10)
			if request.POST.get('vegetarian') != 'vegetarian':
				foods = foods.exclude(vegetarian=True)
			if request.POST.get('non_vegetarian') != 'non_vegetarian':
				foods = foods.exclude(vegetarian=False)
			# Return a random food that meets all requirements
			context_dict = {"food": random.choice(foods)}
			context_dict["restaurant"] = context_dict["food"].restaurant
			return render(request, 'whats_for_dinner/result.html', context_dict)
		except:
			# No food selected
			return render(request, 'whats_for_dinner/result.html')
	# Return to home page
	return render(request, 'whats_for_dinner/index.html')


def register(request):
	registered = False
	# Register using form
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print(user_form.errors)
	else:
		user_form = UserForm()
	return render(request, 'whats_for_dinner/register.html', {'user_form': user_form, 'registered': registered})


def log_in(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your account is disabled.")
		else:
			return render(request, 'whats_for_dinner/login.html', {'message': 'Invalid login details. Please try again.'})
	else:
		return render(request, 'whats_for_dinner/login.html', {})


@login_required
def favourites(request):
	# Get or create user favorites
	user_favourites = UserFavourites.objects.get_or_create(user=request.user)[0]
	foods = user_favourites.favourites.all()
	# Return favourite foods if exist
	if foods:
		return render(request, 'whats_for_dinner/myfavourites.html', {"foods": foods})
	return render(request, 'whats_for_dinner/myfavourites.html')


@login_required
def modify(request):
	if request.method == 'POST':
		context_dict = {'postcode': request.POST.get('postcode')}
		# Get and return all nearby foods and nearby favourites
		try:
			restaurants = get_restaurants(request.POST.get('postcode'))
			foods = Food.objects.filter(restaurant__in=restaurants)
			user_favourites = UserFavourites.objects.get(user=request.user)
			favourite_foods = user_favourites.favourites.all()
			context_dict['foods'] = foods
			context_dict['favourites'] = favourite_foods
		except:
			print('Error in modify request')
		return render(request, 'whats_for_dinner/modify.html', context_dict)
	return render(request, 'whats_for_dinner/modify.html')


@login_required
def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


# Helper function to get restaurants near a postcode using Google Maps
def get_restaurants(postcode):
	try:
		gmaps = googlemaps.Client(key='AIzaSyA-9Fdrh8xBrV9gu-aMQ7wHmBYtjt0YWh0')
		location = gmaps.geocode(postcode + ', UK')[0]['geometry']['location']
		lat_range = (location['lat'] - 0.0045, location['lat'] + 0.0045,)
		lng_range = (location['lng'] - 0.0080, location['lng'] + 0.0080,)
		restaurants = Restaurant.objects.filter(latitude__gte=lat_range[0], latitude__lte=lat_range[1],
		                                        longitude__gte=lng_range[0], longitude__lte=lng_range[1])
	except:
		print('Google Maps Geocoding error')
		return None
	return restaurants
