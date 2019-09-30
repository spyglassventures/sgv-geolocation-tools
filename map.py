# import libraries
import folium # pip install folium
import pandas as pd

from IPython import embed


import webbrowser, os


## Get location an GPS coordinates
## pip install geopy
from geopy.geocoders import Nominatim
from geopy import GoogleV3
geolocator = Nominatim(user_agent="specify_your_app_name_here")
#location = geolocator.geocode("175 5th Avenue NYC")
where = input("Enter lookup address: ")

try:
  location = geolocator.geocode(where)
  print("..............................")
  print("Best match avialable:")
  print(location.address)
  print((location.latitude, location.longitude))
  #place = "221b Baker Street, London"
  #location = GoogleV3().geocode(place)         # needs api key
  #print(location.address)                      #
  #print(location.location)                     #
except:
  print("Address not found")

# Make a data frame with dots to show on the map

data = pd.DataFrame({
'lat':[location.longitude],
'lon':[location.latitude],
'name':[location.address]
})
data

#embed()

# Make an empty map
m = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)

# I can add marker one by one on the map
for i in range(0,len(data)):
    folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name']).add_to(m)

# Save it as html
m.save('SearchLocation.html')


## Show location of your ISP
import requests
print ("")
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
print ("Your IP and location:")
print(my_ip)
print ("")
# Prints The IP string, ex: 198.975.33.4
# Step 2) Look up the GeoIP information from a database for the user's ip
geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()
print(geo_data)
print ("")

# Make a data frame with dots to show on the map
data = pd.DataFrame({
    'lat': [geo_data.get('longitude')],
    'lon': [geo_data.get('latitude')],
    'name': [geo_data.get('city')]
})
data

# Make an empty map
m = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)

# I can add marker one by one on the map
for i in range(0, len(data)):
    folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name']).add_to(m)

# Save it as html
m.save('ISP_map.html')



# For Emoticon
import emoji

# Progress bar:
import time
import progressbar
print(emoji.emojize('Compiling map. Made in Switzerland with :fire:', use_aliases=True))
def custom_len(value):
    # These characters take up more space
    characters = {}
    total = 0
    for c in value:
        total += characters.get(c, 1)
    return total
bar = progressbar.ProgressBar(
    widgets=[
        'Progress',
        progressbar.Bar(),
        ' ',
        progressbar.Counter(format='%(value)02d/%(max_value)d'),
    ],
    len_func=custom_len,
)
for i in bar(range(1)):
    time.sleep(0.1)


# Open in Browser
#ebbrowser.open('file://' + os.path.realpath('/Users/danielmueller/learningcenter/bored/SearchLocation.html'))
webbrowser.open('file://' + os.path.realpath('SearchLocation.html'))
