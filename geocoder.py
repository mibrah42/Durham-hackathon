from geopy.geocoders import Nominatim
locator = Nominatim()
location = locator.geocode("2327 WINLORD PL")
print((location.latitude, location.longitude))
