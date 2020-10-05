from django.urls import path,include
from . import views

app_name = 'map'

urlpatterns = [
        path('',views.home,name='home_new'),
        path('map',views.map,name='map'),
        path('folium',views.folium_map,name="folium_map"),
        path('mapex',views.mapex,name='mapex'),
        # path('index' , views.index_map , name='index'),
]
