"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

from urllib.request import urlopen
import json
from pprint import pprint
from geopy.distance import vincenty

# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    # url = "https://maps.googleapis.com/maps/api/geocode/json?address=Fenway%20Park"
    f = urlopen(url)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    return response_data



def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    myString = place_name.replace(" ", "+")
    url = GMAPS_BASE_URL + "?address=" + myString
    response_data = get_json(url)
    pprint(response_data)
    lat = response_data['results'][0]['geometry']['location']['lat']
    lon = response_data['results'][0]['geometry']['location']['lng']

    return (lat, lon)


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """

    pass
    url = MBTA_BASE_URL + "?api_key=" + MBTA_DEMO_API_KEY + "&lat=" + latitude + "&lon=" + longitude + "&format=json"
    response_data = get_json(url)
    pprint(response_data)
    if(len(response_data['stop']) < 1):
        print('Out of Range')
        return (0, 'N/A')

    name = response_data['stop'][0]['stop_name']
    return (response_data['stop'][0]['distance'], name)


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the
    distance from the given place to that stop.
    """
    mytup = get_lat_long(place_name)
    mytup = get_nearest_station(str(mytup[0]), str(mytup[1]))
    response = str(mytup[1]) + ' is only ' + str(mytup[0]) + ' miles away from ' + place_name
    print(response)
    # return get_nearest_station(str(mytup[0]), str(mytup[1]))


if __name__ == '__main__':
    # url = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA"
    # pprint(get_lat_long("1600 Amphitheatre Parkway, Mountain View, CA"))

    find_stop_near('Saint Simons Island')
