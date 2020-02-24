from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
import json
from os import getenv

categories = ['Accounting', 'Airport', 'Amusement_park', 'Aquarium', 'Art_gallery', 'Atm', 'Bakery', 'Bank', 'Bar', 'Beauty_salon', 'Bicycle_store', 'Book_store', 'Bowling_alley', 'Bus_station', 'Cafe', 'Campground', 'Car_dealer', 'Car_rental', 'Car_repair', 'Car_wash', 'Casino', 'Cemetery', 'Church', 'City_hall', 'Clothing_store', 'Convenience_store', 'Courthouse', 'Dentist', 'Department_store', 'Doctor', 'Electrician', 'Electronics_store', 'Embassy', 'Fire_station', 'Florist', 'Funeral_home', 'Furniture_store', 'Gas_station', 'Gym', 'Hair_care', 'Hardware_store', 'Hindu_temple', 'Home_goods_store', 'Hospital', 'Insurance_agency', 'Jewelry_store', 'Laundry', 'Lawyer', 'Library', 'Liquor_store', 'Local_government_office', 'Locksmith', 'Lodging', 'Meal_delivery', 'Meal_takeaway', 'Mosque', 'Movie_rental', 'Movie_theater', 'Moving_company', 'Museum', 'Night_club', 'Painter', 'Park', 'Parking', 'Pet_store', 'Pharmacy', 'Physiotherapist', 'Plumber', 'Police', 'Post_office', 'Real_estate_agency', 'Restaurant', 'Roofing_contractor', 'Rv_park', 'School', 'Shoe_store', 'Shopping_mall', 'Spa', 'Stadium', 'Storage', 'Store', 'Subway_station', 'Supermarket', 'Synagogue', 'Taxi_stand', 'Train_station', 'Transit_station', 'Travel_agency', 'Veterinary_care', 'Zoo']
result = {
   "html_attributions" : [],
   "next_page_token" : "CuQEUgIAAKKtqmmiLBf2b2O89A6w1iSROoL6YuG61FOq_DpsuOZME_60TnL67ZJJUDKLIysaPJk27o17-PwSquOk345Bp9Nc3fWkc2uF-sjoqaEt0xpGw6HPgNmlLe5lyiV2Sw-i_ygU99-cFsfEiE51De2LPpCaBv0M88LzCjJq7zQnkzAdxfMBytNZUnN5sOqDXzKKa9fwgr-6Jjugyd8wrVKyZV1zbN50xC7KqP3BYQ3QXCoF3fJsmfYPtnoifM_4pJCmXqwqbgmTYSF-BQeEu5v1fzJuewuNrziM2pyA1g9V-Wwuehne4iiu5MwaAC0a8V5UwB54F29O4NnuTiOM3ae8DxfsD_t74_0sIPsiVa0B8DIRupt3EjWXJXrQ3HzQP7IyIQI8vCNnGrDmKJGn75nDgQS-epDMP49ixVBcL1c8Z3nB5S01rIbDcFCdOZnYot3w4rBSDdg4gcQBS1fzOR_o1iEf8v8gcAGGrfjmPLM3Z3mTWsCt39UOY69Qh4SX8529Rsq0MCcb5eo2pGH18-ulZ2Ox_QGfU00CHWeTAVqh7qT1tKwxUWqcqEp8Hi8ADX3olzNiuBso9WXfD_DYmfToj1PG-dL3v8Eik43zF27cafCGtXMvu0_i8UUCANWVLtOG7JEgdwps5PEqMT03gP0O-26Yh8l9AjfFv4cxGC56GtfJ2A-vqZF4Gqlq4t2rUOrvc_uPPHIBandhpXTcMGS_N8GTXg-eeZSPEz5au7QhLIY8bfSqqfqPqiG3vQAMCc9h4OFv1rUUmUCiz_ADPAd143MLgwmvhL7NeFuA9XGjwlUIEhClDlHwOc3LhwhLHopDq-KlGhTQQcPSUeOuEMHFsX4aY3r2NeF5Rg",
   "results" : [
      {
         "formatted_address" : "Dhaka 1230, Bangladesh",
         "geometry" : {
            "location" : {
               "lat" : 23.8660287,
               "lng" : 90.38868859999999
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 23.86737892989272,
                  "lng" : 90.39004342989271
               },
               "southwest" : {
                  "lat" : 23.86467927010728,
                  "lng" : 90.38734377010728
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/atm-71.png",
         "id" : "08749f1021d23da353c043527ba0855f270caf79",
         "name" : "BRAC Bank Limited | ATM Booth",
         "place_id" : "ChIJyyQF2hvEVTcRA96V0gOEGpw",
         "plus_code" : {
            "compound_code" : "V98Q+CF Dhaka",
            "global_code" : "7MMGV98Q+CF"
         },
         "rating" : 4.2,
         "reference" : "ChIJyyQF2hvEVTcRA96V0gOEGpw",
         "types" : [ "atm", "finance", "point_of_interest", "establishment" ],
         "user_ratings_total" : 9
      },
      {
         "formatted_address" : "Gausul Azam Ave, Dhaka 1230, Bangladesh",
         "geometry" : {
            "location" : {
               "lat" : 23.8692652,
               "lng" : 90.3896458
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 23.87064877989272,
                  "lng" : 90.39099497989272
               },
               "southwest" : {
                  "lat" : 23.86794912010728,
                  "lng" : 90.38829532010729
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/atm-71.png",
         "id" : "8f2c6557936478df45363a86befa43ed249dda46",
         "name" : "Jamuna Bank Limited | ATM Booth",
         "photos" : [
            {
               "height" : 3120,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/100383875389957339513\"\u003eMohammad Tushar Bhuyan\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAASssodjzHCtLt0Shk-dt6yJMjYKiJUtJDEkDwckWQMZcoA5sNF4lq2jgMlD2vowIvOtQXlnifdZdsE8ISm0T8IHfJb1MfJTzsH6ilY1CEzUs3UeJSOp6QY2V4HE3qvR1YEhBLWx38cN6JhVF49psbexgkGhR-W2HeCP0v4YRlJmMhpaU8xgstpQ",
               "width" : 4160
            }
         ],
         "place_id" : "ChIJfycR5RnEVTcRnF73KyRkmv8",
         "plus_code" : {
            "compound_code" : "V99Q+PV Dhaka",
            "global_code" : "7MMGV99Q+PV"
         },
         "rating" : 4.1,
         "reference" : "ChIJfycR5RnEVTcRnF73KyRkmv8",
         "types" : [ "atm", "finance", "point_of_interest", "establishment" ],
         "user_ratings_total" : 8
      },
      {
         "formatted_address" : "78 Gausul Azam Ave, Dhaka 1230, Bangladesh",
         "geometry" : {
            "location" : {
               "lat" : 23.8694313,
               "lng" : 90.38532719999999
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 23.87073932989272,
                  "lng" : 90.38667867989271
               },
               "southwest" : {
                  "lat" : 23.86803967010728,
                  "lng" : 90.38397902010728
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/atm-71.png",
         "id" : "8f3f49af20f0a9998b9837f48a7870539588987e",
         "name" : "Dutch Bangla Bank Fast Track",
         "photos" : [
            {
               "height" : 2340,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/103632912572920085812\"\u003eaziz ullah\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAAS9yVPLSaDMg2YERn-J9GeMWLWpKPYaFJmorgCDwWxzpPQL4-ik3VMmSz2BJY67Fn1VMP8397He7aZfaag5LBynCWzVoK_9fN34bhyziqyJzlGGaxWc6doM9uPKe_Mt9bEhBnBipPp0t3ZKKrKFVNf7HVGhQRV0bDXAZIrcX7gycnbJpYn0BACw",
               "width" : 4160
            }
         ],
         "place_id" : "ChIJf0hRGfjFVTcR4JszpTvQ8aU",
         "plus_code" : {
            "compound_code" : "V99P+Q4 Dhaka",
            "global_code" : "7MMGV99P+Q4"
         },
         "rating" : 5,
         "reference" : "ChIJf0hRGfjFVTcR4JszpTvQ8aU",
         "types" : [ "atm", "finance", "point_of_interest", "establishment" ],
         "user_ratings_total" : 1
      },
      {
         "formatted_address" : "Gareeb-e-Nawaz Ave, Dhaka 1230, Bangladesh",
         "geometry" : {
            "location" : {
               "lat" : 23.8704014,
               "lng" : 90.3910513
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 23.87174977989272,
                  "lng" : 90.39234037989272
               },
               "southwest" : {
                  "lat" : 23.86905012010728,
                  "lng" : 90.38964072010728
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/atm-71.png",
         "id" : "d723230e7f0bae96cc730ab074f7fb0ea701dd7a",
         "name" : "First Security Islami Bank Limited | ATM Booth",
         "photos" : [
            {
               "height" : 1836,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/104857557824779624899\"\u003eRedwan Hasan\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAAEEAbWKA5ybLqWDMSNI9-86xVW0-mucleg-H2EdmiV-_1qOXpeeWtMyXggOxFgkayhmf0xIgugagwyUTM33wMKbA1_nOBQOapyuaa-PgzgDKLwqqs4ieBj7fhGpquPkjgEhC_P3U4CRwjMDr8PgelR743GhSnpLnRFOQo7GCLBfAOf-p8OCQNfQ",
               "width" : 3264
            }
         ],
         "place_id" : "ChIJITS2exfEVTcRg__zxvjiAO0",
         "plus_code" : {
            "compound_code" : "V9CR+5C Dhaka",
            "global_code" : "7MMGV9CR+5C"
         },
         "rating" : 3.8,
         "reference" : "ChIJITS2exfEVTcRg__zxvjiAO0",
         "types" : [ "atm", "finance", "point_of_interest", "establishment" ],
         "user_ratings_total" : 6
      },
      {
         "formatted_address" : "Sonargaon Janapath, Dhaka 1230, Bangladesh",
         "geometry" : {
            "location" : {
               "lat" : 23.8740772,
               "lng" : 90.3909149
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 23.87542662989272,
                  "lng" : 90.39223397989272
               },
               "southwest" : {
                  "lat" : 23.87272697010728,
                  "lng" : 90.38953432010727
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/atm-71.png",
         "id" : "af9900724d62332455860d71337a457002796b0d",
         "name" : "City Bank Limited | ATM Booth",
         "place_id" : "ChIJ2cK58xbEVTcRD8wKTGiKwyo",
         "plus_code" : {
            "compound_code" : "V9FR+J9 Dhaka",
            "global_code" : "7MMGV9FR+J9"
         },
         "rating" : 5,
         "reference" : "ChIJ2cK58xbEVTcRD8wKTGiKwyo",
         "types" : [ "atm", "finance", "point_of_interest", "establishment" ],
         "user_ratings_total" : 1
      },
      {
         "formatted_address" : "Gareeb-e-Nawaz Ave, Dhaka 1230, Bangladesh",
         "geometry" : {
            "location" : {
               "lat" : 23.8760571,
               "lng" : 90.3906238
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 23.87740722989273,
                  "lng" : 90.39201662989274
               },
               "southwest" : {
                  "lat" : 23.87470757010728,
                  "lng" : 90.38931697010729
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/atm-71.png",
         "id" : "c76b41cca46b365feeebc862fd56ab7ad0998259",
         "name" : "Prime Bank Limited | ATM Booth",
         "photos" : [
            {
               "height" : 4096,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/100001878937832400193\"\u003eShahnewaz Razu\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAATlSEVA6-mWQ18K4JqoUrp8UsZWPKS1zvAvJ6vfgEPio8yeyXQZXhNRNKxc0z03r1wlgPswMWPIhZMxBczTZSt9m-PlvqoKHkM-N9zl2sHMcaQHQPTUkgmWOi2ExvIRXBEhCGQDm7WMWf2Kts4r8D7Bw7GhSvyPnxgHXFIU1KQWKl2hDD-d8dpw",
               "width" : 2304
            }
         ],
         "place_id" : "ChIJmbOJJhTEVTcRz__6FyAGhhg",
         "plus_code" : {
            "compound_code" : "V9GR+C6 Dhaka",
            "global_code" : "7MMGV9GR+C6"
         },
         "rating" : 3.9,
         "reference" : "ChIJmbOJJhTEVTcRz__6FyAGhhg",
         "types" : [ "atm", "finance", "point_of_interest", "establishment" ],
         "user_ratings_total" : 7
      },
      {
         "formatted_address" : "7 Gareeb-e-Nawaz Ave, Dhaka 1230, Bangladesh",
         "geometry" : {
            "location" : {
               "lat" : 23.8745996,
               "lng" : 90.39070459999999
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 23.87594932989273,
                  "lng" : 90.39204942989272
               },
               "southwest" : {
                  "lat" : 23.87324967010728,
                  "lng" : 90.38934977010729
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/atm-71.png",
         "id" : "7bdc4d0560c111cc9a1d47cc8d4d36c8b1f16ca8",
         "name" : "ATM Al Arafah Islami Bank Ltd.",
         "photos" : [
            {
               "height" : 3024,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/117286405613972585414\"\u003eAbdullah Ferdous\u003c/a\u003e"
               ],
               "photo_reference" : "CmRZAAAADFb30KfGgiCG89WYpC8VVq7-Y8cZ5XtKeHln8-oHM3F6MBv3kionierahSD_sL0r-0p3q1fzsU8y1CZwKISvdth1_2I7E4BMlvWUp6yeEdO7YtSV4-q_8LHlPnE7C0wbEhCutykdZyVdgPY0J-9jbQD3GhQ8axOV9tFv0tltoNSNpDARLerzlQ",
               "width" : 4032
            }
         ],
         "place_id" : "ChIJ3cNzkhbEVTcRHhfvm-7Lho0",
         "plus_code" : {
            "compound_code" : "V9FR+R7 Dhaka",
            "global_code" : "7MMGV9FR+R7"
         },
         "rating" : 4,
         "reference" : "ChIJ3cNzkhbEVTcRHhfvm-7Lho0",
         "types" : [ "atm", "finance", "point_of_interest", "establishment" ],
         "user_ratings_total" : 4
      }
   ],
   "status" : "OK"
}
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

   # return HttpResponse(coordinates, content_type='application/json')

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
   print(data['result'])
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
