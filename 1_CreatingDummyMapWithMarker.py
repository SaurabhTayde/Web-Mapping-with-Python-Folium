import folium

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = 'Stamen Terrain')

fg = folium.FeatureGroup(name = 'My Map')

fg.add_child(folium.Marker(location = [38.2,-99.1], popup = 'Hi, I am a Marker', icon = folium.Icon(color = 'green')))

map.add_child(fg)

map.save('1_CreatingDummyMapWithMarker.html')
