from geopy.geocoders import Nominatim

def coords(adress):
    '''
    :param adress: the adress (examp. Lviv, NYC...)
    :return: [int, int] coordinates of the location
    '''
    geolocator = Nominatim()
    location = geolocator.geocode(adress)
    return [location.latitude, location.longitude]
