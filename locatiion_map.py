from get_locations import *
from find_coordinates import *
import folium

def map(file):
    '''
    :param file: a name of a file with info
    :return: none
    func takek coordinations and names
    generete html map according to the term
    '''
    locations = locations_getter(file)
    map = folium.Map(location = [49.85, 24.0166666667], zoom_start = 1)
    fg = folium.FeatureGroup(name = "Twitter friends locations")
    for i in locations:
        coordinates = coords(i[1])
        fg.add_child(folium.Marker(location=coordinates, popup = i[0]))
    map.add_child(fg)
    map.save('friends_locaton.html')