from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
import json
from os import getenv

categories = ['Accounting', 'Airport', 'Amusement_park', 'Aquarium', 'Art_gallery', 'Atm', 'Bakery', 'Bank', 'Bar', 'Beauty_salon', 'Bicycle_store', 'Book_store', 'Bowling_alley', 'Bus_station', 'Cafe', 'Campground', 'Car_dealer', 'Car_rental', 'Car_repair', 'Car_wash', 'Casino', 'Cemetery', 'Church', 'City_hall', 'Clothing_store', 'Convenience_store', 'Courthouse', 'Dentist', 'Department_store', 'Doctor', 'Electrician', 'Electronics_store', 'Embassy', 'Fire_station', 'Florist', 'Funeral_home', 'Furniture_store', 'Gas_station', 'Gym', 'Hair_care', 'Hardware_store', 'Hindu_temple', 'Home_goods_store', 'Hospital', 'Insurance_agency', 'Jewelry_store', 'Laundry', 'Lawyer', 'Library', 'Liquor_store', 'Local_government_office', 'Locksmith', 'Lodging', 'Meal_delivery', 'Meal_takeaway', 'Mosque', 'Movie_rental', 'Movie_theater', 'Moving_company', 'Museum', 'Night_club', 'Painter', 'Park', 'Parking', 'Pet_store', 'Pharmacy', 'Physiotherapist', 'Plumber', 'Police', 'Post_office', 'Real_estate_agency', 'Restaurant', 'Roofing_contractor', 'Rv_park', 'School', 'Shoe_store', 'Shopping_mall', 'Spa', 'Stadium', 'Storage', 'Store', 'Subway_station', 'Supermarket', 'Synagogue', 'Taxi_stand', 'Train_station', 'Transit_station', 'Travel_agency', 'Veterinary_care', 'Zoo']

# Create your views here.
def index(request):
   # search_places('dhaka', 5000, 'atm')
   return render(request, 'maps/index.html', {'coordinates':[], 'categories':categories})

def query(request):
   address = request.GET.get('address')
   category = request.GET.get('category').lower()
   data = search_places(address, 5000, category)
   coordinates = {}
   for place in data["results"]:
      coordinates[place['place_id']] = place['geometry']['location']

   return JsonResponse(json.dumps(coordinates), safe=False)

def search_places(address, radius, types):
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        data = {
            'query': address,
            'radius': radius,
            'types': types,
            'key': getenv('MAPS_KEY')
        }
        res = requests.get(url, params = data)
        response = json.loads(res.content)
        return response

def details(request):
   place_id = request.GET.get('place_id')
   fields = ['name', 'formatted_address', 'formatted_phone_number', 'geometry', 'international_phone_number', 'rating', 'reviews', 'url', 'website', 'opening_hours']
   data = get_place_details(place_id, fields)

   return JsonResponse(json.dumps(data['result']), safe=False)

def get_place_details(place_id, fields):
        url = "https://maps.googleapis.com/maps/api/place/details/json"
        data = {
            'place_id': place_id,
            'fields': ",".join(fields),
            'key': getenv('MAPS_KEY')
        }
        res = requests.get(url, params = data)
        place_details =  json.loads(res.content)
        return place_details
