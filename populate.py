import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wfd.settings')

import googlemaps
import django
django.setup()
from whats_for_dinner.models import *


def populate():

	foods_38135 = [
		{"name": 'Margherita 5"', "price": 4.45, "vegetarian": True,
			"description": "A thin base topped with tomato & mozzarella cheese"},
		{"name": 'Margherita 12"', "price": 7.45, "vegetarian": True,
			"description": "A thin base topped with tomato & mozzarella cheese"},
		{"name": 'Margherita 16"', "price": 10.45, "vegetarian": True,
			"description": "A thin base topped with tomato & mozzarella cheese"},
		{"name": 'Italiano 5"', "price": 5.25, "vegetarian": False,
			"description": "Crumbled Italian sausage & pepperoni sausage on a thin base pizzette pizza with sprinkled mozzarella"},
		{"name": 'Italiano 12"', "price": 9.45, "vegetarian": False,
			"description": "Crumbled Italian sausage & pepperoni sausage on a thin base pizzette pizza with sprinkled mozzarella"},
		{"name": 'Italiano 16"', "price": 12.45, "vegetarian": False,
			"description": "Crumbled Italian sausage & pepperoni sausage on a thin base pizzette pizza with sprinkled mozzarella"},
		{"name": 'Pizza Cassino 16"', "price": 14.95, "vegetarian": False,
			"description": "With crumbled Italian sausage & sliced pepperoni"},
		{"name": 'Pizza San Pietro 16"', "price": 14.95, "vegetarian": False,
			"description": "With chicken breast & wild field mushrooms"},
		{"name": 'Pennette Salsiccia', "price": 8.45, "vegetarian": False,
			"description": "Italian crumbled sausage & sliced pepperoni sausage pan fried with pesto & garlic tossed in a Romano sauce of tomato & cream, mixed with De Cecco penne pasta"},
		{"name": 'Fusilli Rosso', "price": 8.45, "vegetarian": True,
			"description": "Red pesto & mascarpone cheese sauce, served with rocket & fresh parmesan cheese mixed with twisty De Cecco pasta"},
		{"name": 'Calamari Fritti', "price": 4.15, "vegetarian": False,
			"description": "Squid rings tossed in seasoned flour deep fried & served with a wedge of fresh lemon & garlic mayonnaise dip"},
		{"name": 'Cacciucco', "price": 5.95, "vegetarian": False,
			"description": "Mixed seafood Italian stew slowly cooked in a san marzano sauce with fresh basil & red chilli"},
		{"name": 'Pork Belly', "price": 4.25, "vegetarian": False,
			"description": "World famous Ramsey of Carluke pork belly chargrilled & oven roasted, drizzled with balsamic vinegar"},
	]

	foods_73335 = [
		{"name": 'Chicken Katsu Curry Bowl', "price": 7.80, "vegetarian": False,
			"description": ""},
		{"name": 'Chicken Teriyaki Bowl', "price": 7.80, "vegetarian": False,
			"description": ""},
		{"name": 'Salmon Feast Set', "price": 11.00, "vegetarian": False,
			"description": "4 Salmon & avocado roll\n2 Grilled salmon roll\n4 Salmon maki\n3 Salmon nigiri\n3 Salmon sashimi\nEdamame beans"},
		{"name": 'Veggie Set', "price": 6.25, "vegetarian": True,
			"description": "2 Cucumber maki\n2 Pickle maki\n2 Tofu nigiri\n2 Avocado maki\n2 Yasai roll\nEdamame beans"},
		{"name": 'Classic Beef Bowl', "price": 8.50, "vegetarian": False,
			"description": ""},
		{"name": 'Yasai Tempura Bowl', "price": 7.80, "vegetarian": True,
			"description": ""},
		{"name": 'Classic Tonkotsu Ramen', "price": 8.80, "vegetarian": False,
			"description": ""},
		{"name": 'Sapporo Miso Ramen', "price": 8.80, "vegetarian": False,
			"description": ""},
		{"name": 'Sirloin Steak Poke Bowl', "price": 10.50, "vegetarian": False,
			"description": ""},
		{"name": 'Tuna Poke Bowl', "price": 10.50, "vegetarian": False,
			"description": ""},
		{"name": 'California Roll 4 pieces', "price": 4.60, "vegetarian": False,
			"description": ""},
		{"name": 'California Roll 8 pieces', "price": 8.90, "vegetarian": False,
			"description": ""},
		{"name": 'Grilled Eel Roll 8 pieces', "price": 11.00, "vegetarian": False,
			"description": ""},
	]

	foods_15990 = [
		{"name": 'Puri Chana (Chickpeas)', "price": 4.25, "vegetarian": True,
			"description": "Light thin deep fried chapati"},
		{"name": 'Puri Chicken', "price": 4.50, "vegetarian": False,
			"description": "Light thin deep fried chapati"},
		{"name": 'Puri King Prawn', "price": 5.95, "vegetarian": False,
			"description": "Light thin deep fried chapati"},
		{"name": 'Chicken Tikka Main', "price": 10.95, "vegetarian": False,
			"description": "Pieces of chicken marinated in homemade yoghurt, spices & barbecued in the clay oven"},
		{"name": 'Lamb Tikka Main', "price": 12.95, "vegetarian": False,
			"description": "Tender pieces of lamb marinated in yoghurt flavoured with Indian spices & cooked in a clay oven"},
		{"name": 'Kadhai Paneer', "price": 7.95, "vegetarian": True,
			"description": "Homemade cottage cheese simmered in a rich bhuna style with onions & peppers"},
		{"name": 'Daal Tarka', "price": 7.95, "vegetarian": True,
			"description": "Mixed yellow lentils tempered with garlic, ginger & onion"},
		{"name": 'Bombay Aloo', "price": 7.95, "vegetarian": True,
			"description": "Potatoes sauteed in our chef's piquant tomato gravy"},
		{"name": 'Chicken Kolhapuree', "price": 9.95, "vegetarian": False,
			"description": "Chicken pieces cooked with garlic, ginger, tomato & a variety of different masalas to give that authentic taste"},
		{"name": 'Lucknowi Murgh', "price": 9.95, "vegetarian": False,
			"description": "Breast of chicken, simmered in a mild, creamy tomato sauce"},
		{"name": 'Butter Chicken', "price": 9.95, "vegetarian": False,
			"description": "Tandoori chicken breast, gently poached in a buttery tomato sauce flavoured with fenugreek"},
		{"name": 'Tikka Masala Chicken', "price": 8.50, "vegetarian": False,
			"description": "Flavoursome fusion of ginger, garlic, peppers & onions"},
		{"name": 'Tikka Masala King Prawn', "price": 12.50, "vegetarian": False,
			"description": "Flavoursome fusion of ginger, garlic, peppers & onions"},
		{"name": 'Tikka Masala Lamb', "price": 8.95, "vegetarian": False,
			"description": "Flavoursome fusion of ginger, garlic, peppers & onions"},
		{"name": 'Tikka Masala Vegetable', "price": 7.95, "vegetarian": True,
			"description": "Flavoursome fusion of ginger, garlic, peppers & onions"},
		{"name": 'Biryani Chicken', "price": 10.95, "vegetarian": False,
			"description": "A traditional dish from Hyderabad, simmered in basmati rice with a host of aromatic spices, cardamom, saffron, fenugreek & garnished with coriander"},
		{"name": 'Biryani Lamb', "price": 11.95, "vegetarian": False,
			"description": "A traditional dish from Hyderabad, simmered in basmati rice with a host of aromatic spices, cardamom, saffron, fenugreek & garnished with coriander"},
		{"name": 'Biryani Vegetable', "price": 9.95, "vegetarian": True,
			"description": "A traditional dish from Hyderabad, simmered in basmati rice with a host of aromatic spices, cardamom, saffron, fenugreek & garnished with coriander"},
	]

	foods_72633 = [
		{"name": 'Peking Ribs', "price": 5.90, "vegetarian": False,
			"description": ""},
		{"name": 'Sesame Prawn on Toast', "price": 5.90, "vegetarian": False,
			"description": ""},
		{"name": 'Chicken Satay on Skewers', "price": 6.30, "vegetarian": False,
			"description": ""},
		{"name": 'Quarter Peking Aromatic Duck', "price": 11.40, "vegetarian": False,
			"description": "With spring onions, cucumbers, pancakes & our special sauce"},
		{"name": 'Chicken in Batter', "price": 6.10, "vegetarian": False,
			"description": "With sweet & sour sauce"},
		{"name": 'Beef Chop Suey', "price": 5.70, "vegetarian": False,
			"description": ""},
		{"name": 'Fried Sweet & Sour King Prawn Hong Kong Style', "price": 7.50, "vegetarian": False,
			"description": ""},
		{"name": 'Mushroom Curry', "price": 5.40, "vegetarian": True,
			"description": ""},
		{"name": 'Roast Pork with Black Pepper Sauce', "price": 5.70, "vegetarian": False,
			"description": ""},
		{"name": 'Mixed Vegetables Noodles', "price": 6.50, "vegetarian": True,
			"description": "Stir fry noodles"},
		{"name": 'Special Fried Rice', "price": 7.50, "vegetarian": False,
			"description": ""},
		{"name": 'Singapore Fried Rice', "price": 7.50, "vegetarian": False,
			"description": ""},
		{"name": 'Mix Vegetable in Garlic', "price": 5.50, "vegetarian": True,
			"description": ""},
		{"name": 'Bean Curd Home Style', "price": 7.50, "vegetarian": True,
			"description": ""},
	]

	restaurants = {
		"La Vita Spuntini": {"id": "38135", "address": "199 Byres Road, Glasgow, G12 8TN", "food": foods_38135},
		"Okome": {"id": "73335", "address": "161 Byres Road, Glasgow, G12 8TS", "food": foods_73335},
		"Masala Twist Indian Restaurant": {"id": "15990", "address": "192-194 Byres Road, Glasgow, G12 8SN", "food": foods_15990},
		"Chow": {"id": "72633", "address": "98 Byres Road, Glasgow, G12 8TB", "food": foods_72633},
	}

	gmaps = googlemaps.Client(key='AIzaSyA-9Fdrh8xBrV9gu-aMQ7wHmBYtjt0YWh0')

	for restaurant, restaurant_data in restaurants.items():
		location = gmaps.geocode(restaurant_data["address"])[0]['geometry']['location']
		r = add_restaurant(restaurant, restaurant_data["id"], restaurant_data["address"],
							location["lat"], location["lng"])
		for f in restaurant_data["food"]:
			add_food(f["name"], r, f["price"], f["vegetarian"], f["description"])

	for r in Restaurant.objects.all():
		for f in Food.objects.filter(restaurant=r):
			print("- {0} - {1}".format(str(r), str(f)))


def add_restaurant(name, id, address, latitude, longitude):
	r = Restaurant.objects.get_or_create(
		name=name, image=id+'.gif', address=address, latitude=latitude, longitude=longitude)[0]
	r.save()
	return r


def add_food(name, restaurant, price, vegetarian, description):
	f = Food.objects.get_or_create(
		name=name, restaurant=restaurant, price=price, vegetarian=vegetarian, description=description)[0]
	f.save()
	return f


if __name__ == '__main__':
	print("Starting population script...")
	populate()
