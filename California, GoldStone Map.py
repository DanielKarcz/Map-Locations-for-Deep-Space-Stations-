#!/usr/bin/env python
# coding: utf-8

# In[22]:


get_ipython().system('pip install ipyleaflet')


# In[23]:


get_ipython().system('jupyter nbextension enable --py --sys-prefix ipyleaflet')


# In[35]:


from ipyleaflet import (Map, DrawControl)
import ipywidgets 
mymap = Map(center=[35.422664976,-116.887329784], zoom =10) 
dc = DrawControl(circle=('shapeOptions':('color':'#0000FF')), rectangle=('shapeOptions':('color':'#0000FF')))
mymap.add_control(dc)
mymap


# In[53]:


radio_button = ipywidgets.RadioButtons(options=['Positron', 'DarkMatter', 'WorldStreetMap', 'WorldTopoMap',
                                              'WorldImagery', 'NatGeoWorldMap','ModisTerra','OpenTopoMap'], 
                                      value='Positron', description= 'map types:')

# 'Delorme','HikeBike', 'HyddaFull', 'Night','Mapnik', 'HOT', 'Toner', 'Watercolor'


# In[29]:


from ipyleaflet import (Map, DrawControl, basemaps)
import ipywidgets


# In[57]:


def toggle_maps(map):
    if map == 'Positron': m = Map(zoom=2, basemap=basemaps.CartoDB.Positron)
    if map == 'DarkMatter': m = Map(zoom =1, basemap=basemaps.CartoDB.DarkMatter)
    if map == 'WorldStreetMap': m = Map(center=[35.422664976,-116.887329784],zoom =10,basemap=basemaps.Esri.WorldStreetMap)
    if map == 'WorldTopoMap': m = Map(center=[35.422664976,-116.887329784],zoom =10,basemap=basemaps.Esri.WorldTopoMap)
    if map == 'WorldImagery': m = Map(center=[35.422664976,-116.887329784],zoom =10,basemap=basemaps.Esri.WorldImagery)
    if map == 'NatGeoWorldMap': m = Map(center=[35.422664976,-116.887329784],zoom =10,basemap=basemaps.Esri.NatGeoWorldMap)
    if map == 'ModisTerra': m = Map(center=[35.422664976,-116.887329784],zoom =9,basemap=basemaps.NASAGIBS.ModisTerraTrueColorCR)
    if map == 'OpenTopoMap': m = Map(center=[35.422664976,-116.887329784],zoom =7,basemap=basemaps.OpenTopoMap)
    #if map == 'HikeBike': m = Map(zoom)
    #if map == 'HyddaFull': m = Map(zoom)
    #if map == 'Night': m = Map(zoom)
    #if map == 'Mapnik': m = Map(zoom)
    #if map == 'HOT': m = Map(zoom)
    #if map == 'OpenTopoMap': m = Map(zoom)
    #if map == 'Toner': m = Map(zoom)
    #if map == 'Watercolor': m = Map(zoom)
    display(m)
    
ipywidgets.interact(toggle_maps, map=radio_button)
    


# # Deep Space Station Coordinate Data

# In[62]:


# This data was obtained from the "Deep Space Network 301 Coverage and Geometry" NASA publication.
#Table 5. Geodetic Coordinates for DSN Stations With Respect to the WGS 84 Ellipsoid
#Antenna latitude (longitude (height(h)
#Name Description deg min sec deg min sec (m)
#DSS 13 34-m R & D 35 14 49.79131 243 12 19.94761 1070.444
#DSS 14 70-m 35 25 33.24312 243 6 37.66244 1001.390
#DSS 15 34-m HEF 35 25 18.67179 243 6 46.09762 973.211
#DSS 24 34-m BWG 35 20 23.61416 243 7 30.74007 951.499
#DSS 25 34-m BWG 35 20 15.40306 243 7 28.69246 959.634
#DSS 26 34-m BWG 35 20 8.48118 243 7 37.14062 968.686
#DSS 342 34-m BWG –35 23 54.52383 148 58 55.07191 692.020
#DSS 352 34-m BWG −35 23 44.86387 148 58 53.24088 694.897
#DSS 362 34-m BWG −35 23 42.36634 148 58 42.75912 685.503
#DSS 43 70-m –35 24 8.72724 148 58 52.56231 688.867
#DSS 45 34-m HEF –35 23 54.44766 148 58 39.66828 674.347
#DSS 54 34-m BWG 40 25 32.23805 355 44 45.25141 837.051
#DSS 55 34-m BWG 40 25 27.46525 355 44 50.52012 819.061
#DSS 63 70-m 40 25 52.35510 355 45 7.16924 864.816
#DSS 65 34-m HEF 40 25 37.94289 355 44 57.48397 833.854
#Notes:
#1. Geoidal separation must be subtracted from WGS 84 height to get MSL height.
#2. Latitude, longitude, and height absolute accuracy estimated to be +/-0.001 sec and +/-3 cm
#(0.030 m) (1-sigma)
#3. For southern hemisphere antennas deg, min, sec should all be considered negati


# In[59]:


# This data was obtained from the "Deep Space Network 301 Coverage and Geometry" NASA publication.

#Table 2. Cartesian Coordinates for DSN Stations in ITRF93 Reference Frame, Epoch 2003.0
#Antenna1 Cartesian Coordinates
#Name Description x(m) y(m) z(m)
#DSS 13 34-m R & D –2351112.659 –4655530.636 +3660912.728
#DSS 14 70-m –2353621.420 –4641341.472 +3677052.318
#DSS 15 34-m HEF –2353538.958 –4641649.429 +3676669.984
#DSS 24 34-m BWG –2354906.711 –4646840.095 +3669242.325
#DSS 25 34-m BWG –2355022.014 –4646953.204 +3669040.567
#DSS 26 34-m BWG –2354890.797 –4647166.328 +3668871.755
#DSS 341 34-m BWG –4461147.093 +2682439.239 –3674393.133
#DSS 351 34-m BWG −4461273.090 +2682568.925 −3674152.093
#DSS 361 34-m BWG −4461168.415 +2682814.657 −3674083.901
#DSS 43 70-m –4460894.917 +2682361.507 –3674748.152
#DSS 45 34-m HEF –4460935.578 +2682765.661 –3674380.982
#DSS 54 34-m BWG +4849434.488 –360723.8999 +4114618.835
#DSS 55 34-m BWG +4849525.256 –360606.0932 +4114495.084
#DSS 63 70-m +4849092.518 –360180.3480 +4115109.251
#DSS 65 34-m HEF +4849339.634 –360427.6637 +4114750.733
#1. Notes: Position absolute accuracy estimated to be +/−3 cm (0.030 m) (1-sigma) for each coordinate.

# x(m) = distance from the spin axis towards Greenwhich meridian (+x), or towards 180 degree meridian (-x)
# y(m)= distance infront of (+y) or behind (-y) plane (Hour Angle plane) established by the spin axis and
# Greenwhich meridian
# z(m) = height above (+z) or below (-z) equitorial plane


# In[69]:


from ipyleaflet import Map, Marker, MarkerCluster
#install geoecoder first from python.org python package index
import geocoder


################## Practice Code Start ######################################################################################
# Reference = https://www.youtube.com/watch?v=wjzAy_yLrdA
#Location address
#location = geoencoder.osm('2920 Zoo Dr, San Diego, CA, 92101') #type in location.json to see all location data :)
#location.json
#Latitude and Longitutde of location
#latlng = [location.lat, location.long]
#san_diego_zoo_map = Map(center=latlng)
#marker
#marker = Marker(location=latlng, title ='2920 Zoo Dr, San Diego, CA, 92101')
#san_diego_zoo_map.add_layer(marker)
################## Practice Code End ##################################################################################



#Cartesian Coordinate: Description x(m) y(m) z(m)
#DSS 14 70-m –2353621.420 –4641341.472 +3677052.318
#DSS 24 34-m BWG –2354906.711 –4646840.095 +3669242.325
#DSS 25 34-m BWG –2355022.014 –4646953.204 +3669040.567
#DSS 26 34-m BWG –2354890.797 –4647166.328 +3668871.755

#Lat and Long
#DSS 14 70-m 35 25 33.24312 243 6 37.66244  
#DSS 24 34-m BWG 35 20 23.61416 243 7 30.74007  
#DSS 25 34-m BWG 35 20 15.40306 243 7 28.69246  
#DSS 26 34-m BWG 35 20 8.48118 243 7 37.14062  

#marker cluster 
m = Map(center=(35.422664976,-116.887329784),zoom =1)
marker_DSS14 = Marker(location=(35.253324312,243.63766244)) # –2353621.420,–4641341.472 had to shorten, no floats (decimals) allowed
marker_DSS24 = Marker(location=(35.202361416,243.73074007)) #had to shorten, no floats (decimals) allowed
marker_DSS25 = Marker(location=(35.201540306,243.72869246)) #had to shorten, no floats (decimals) allowed
marker_DSS26 = Marker(location=(35.2084118, 243.73714062)) #had to shorten, no floats (decimals) allowed

marker_cluster = MarkerCluster(
    markers=(marker_DSS14, marker_DSS24, marker_DSS25, marker_DSS26)
)

m.add_layer(marker_cluster);

m

#display map
#san_diego_zoo_map


# # Full Screen Control

# In[73]:


from ipyleaflet import FullScreenControl
full_screen_map = Map(zoom=1)
control = FullScreenControl()
full_screen_map.add_control(control)

full_screen_map


# In[75]:


import ipyleaflet
from ipyleaflet import MeasureControl

# create map
measure_control_map = ipyleaflet.Map(zoom=1)

#create control
measure = MeasureControl(position='topleft', active_color='red', primary_length_unit='miles')

#add control to map
measure_control_map.add_control(measure)

# measure line color 
measure_completed_color = 'red'

# display map
measure_control_map


# In[77]:


import ipyleaflet
from ipyleaflet import basemaps, basemap_to_tiles, SplitMapControl

# create map
split_map = ipyleaflet.Map(zoom=1)

#create left and right layers
right_layer = basemap_to_tiles(basemaps.Esri.WorldStreetMap)
left_layer =  basemap_to_tiles(basemaps.NASAGIBS.ViirsEarthAtNight2012)

#create control  
control_split = SplitMapControl(left_layer=left_layer, right_layer=right_layer)

# add control to map
split_map.add_control(control_split)

# display map
split_map


# # Interactive Slider: Plot storms, earthquakes, and wind gusts over time.

# In[78]:


# add in Earthquake data from Kaggle
# add in weather data with lat long coordinates


# In[ ]:




