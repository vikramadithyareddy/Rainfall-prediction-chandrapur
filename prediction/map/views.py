from django.shortcuts import render
import requests,json
import folium
import geopandas,os

def home(request):
    return render(request,'map/home_new.html')

def map(request):
    maha = folium.Map(width=1200,height=650,location=[19,75],
                        zoom_start=7,tiles='cartodbpositron',
                        zoom_control=False,
                        scrollWheelZoom=False,
                        dragging = False,
                        max_zoom=7)
    filename = "maharashtra.geojson"
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = os.path.join(dir_path,filename)
    folium.GeoJson(
        file,
        name='geojson'
    ).add_to(maha)
    #maha.doubleClickZoom.disable()
    m = maha._repr_html_()
    context={'map':m}
    return render(request,'map/map.html',context)

def folium_map(request):
    return render(request,'map/folium_map.html')

def mapex(request):
    return render(request,'map/maps_ex.html')    

def index_map(request):
    return render(request , 'map/index.html')
