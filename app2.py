import folium
import pandas
data = pandas.read_csv("adress.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_changer(elavation):
    if elavation < 1000:
        return 'green'
    elif 1000 <= elavation > 2000:
        return 'black'
    else:
        return 'red'


map = folium.Map(location=[44.4197998, -121.7710037], zoom_start=10)

fgm = folium.FeatureGroup(name="markrs")

for lt, lo, el in zip(lat, lon, elev):
    fgm.add_child(folium.CircleMarker(location=[lt, lo],
                                      popup=folium.Popup(str(el) + 'm.'), radius='10', parse_html=True, fill_color=color_changer(el), color='gray', fill_opacity=0.7))
fgp = folium.FeatureGroup(name="population")

fgp.add_child(folium.GeoJson(
    data=open('king.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor': 'black' if x['properties']['POP2005'] < 10000000
                                                                                        else 'orange'if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgm)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
