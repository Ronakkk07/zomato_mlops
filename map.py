# import folium
# from geopy.geocoders import Nominatim
# import pandas as pd

# zdata = {
#     'Zomato_url': ['https://www.zomato.com/chennai/yaa-mohaideen-briyani-1-pallavaram'],
#     'Name of Restaurent': ['Yaa Mohaideen Briyani'],
#     'Address': ['336 & 338, Main Road, Pallavaram, Chennai'],
# }

# zdata_df = pd.DataFrame(zdata)

# restaurant_map = folium.Map(location=[20.5937, 78.9629], zoom_start=15)  # Increased zoom level for better visibility

# geolocator = Nominatim(user_agent="restaurant_locator")

# for index, restaurant in zdata_df.iterrows():
#     address = restaurant['Address']
#     location = geolocator.geocode(address)
    
#     if location:
#         folium.Marker(
#             location=[location.latitude, location.longitude],
#             popup=f"<b>{restaurant['Name of Restaurent']}</b><br>{address}<br><a href='{restaurant['Zomato_url']}'>Zomato</a>"
#         ).add_to(restaurant_map)

# # Save the map
# restaurant_map.save("restaurant_map.html")
import folium
from geopy.geocoders import Nominatim
import pandas as pd

zdata = {
    'Zomato_url': ['https://www.zomato.com/chennai/yaa-mohaideen-briyani-1-pallavaram'],
    'Name of Restaurent': ['Yaa Mohaideen Briyani'],
    'Address': ['336 & 338, Main Road, Pallavaram, Chennai'],
}

zdata_df = pd.DataFrame(zdata)

restaurant_map = folium.Map(location=[20.5937, 78.9629], zoom_start=15)  # Increased zoom level for better visibility

geolocator = Nominatim(user_agent="restaurant_locator")

for index, restaurant in zdata_df.iterrows():
    address = restaurant['Address']
    location = geolocator.geocode(address)

    if location:
        # Use a red marker
        folium.Marker(
            location=[location.latitude, location.longitude],
            popup=f"<b>{restaurant['Name of Restaurent']}</b><br>{address}<br><a href='{restaurant['Zomato_url']}'>Zomato</a>",
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(restaurant_map)

# Save the map
restaurant_map.save("restaurant_map.html")
