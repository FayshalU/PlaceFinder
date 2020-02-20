# from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
from os import getenv

category = ['accounting', 'airport', 'amusement_park', 'aquarium', 'art_gallery', 'atm', 'bakery', 'bank', 'bar', 'beauty_salon', 'bicycle_store', 'book_store', 'bowling_alley', 'bus_station', 'cafe', 'campground', 'car_dealer', 'car_rental', 'car_repair', 'car_wash', 'casino', 'cemetery', 'church', 'city_hall', 'clothing_store', 'convenience_store', 'courthouse', 'dentist', 'department_store', 'doctor', 'electrician', 'electronics_store', 'embassy', 'fire_station', 'florist', 'funeral_home', 'furniture_store', 'gas_station', 'gym', 'hair_care', 'hardware_store', 'hindu_temple', 'home_goods_store', 'hospital', 'insurance_agency', 'jewelry_store', 'laundry', 'lawyer', 'library', 'liquor_store', 'local_government_office', 'locksmith', 'lodging', 'meal_delivery', 'meal_takeaway', 'mosque', 'movie_rental', 'movie_theater', 'moving_company', 'museum', 'night_club', 'painter', 'park', 'parking', 'pet_store', 'pharmacy', 'physiotherapist', 'plumber', 'police', 'post_office', 'real_estate_agency', 'restaurant', 'roofing_contractor', 'rv_park', 'school', 'shoe_store', 'shopping_mall', 'spa', 'stadium', 'storage', 'store', 'subway_station', 'supermarket', 'synagogue', 'taxi_stand', 'train_station', 'transit_station', 'travel_agency', 'veterinary_care', 'zoo']

# Create your views here.
def index(request):
    # search_places('dhaka', 5000, 'atm')
    return render(request, 'maps/index.html', {})

def search_places(location, radius, types):
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        data = {
            'location': location,
            'radius': radius,
            'types': types,
            'key': getenv('MAPS_KEY')
        }
        res = requests.get(url, params = data)
        results = json.loads(res.content)
        print(results)

def get_place_details(place_id, fields):
        url = "https://maps.googleapis.com/maps/api/place/details/json"
        data = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': getenv('MAPS_KEY')
        }
        res = requests.get(url, params = data)
        place_details =  json.loads(res.content)
        return place_details
