#Liyan Tian
#10/14/2014
#Homework 2
# 5. Write a function to read the topography/bathymetry of the world using the ETOPO5 surface dataset:

# http://www.nio.org/userfiles/file/datainfo/global_merged5.txt

# and return three arrays representing x, y, and z. Write a script using this function to make
# a pcolormesh map of the topo/bathy, and overlay the contours z = [-1000, 0, 1000]. The
# negative contour should be thin and dashed, the 0 contour thick and solid, and the 1000
# contour thin and solid.
from mpl_toolkits.basemap import Basemap,addcyclic
import numpy as np
import matplotlib.pyplot as plt
import netCDF4

map=Basemap(llcrnrlon=-180,llcrnrlat=-80,urcrnrlon=180,urcrnrlat=80,projection='mill')
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
# draw lat/lon grid lines every 30 degrees.
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))
plt.title('contour lines over filled continent background')
nc=netCDF4.Dataset('global_merged5.nc')
topoin = nc.variables['depth'][:]
lons = nc.variables['longitude'][:]
lats = nc.variables['latitude'][:]
topoin, lons = addcyclic(topoin, lons)
lon,lat=np.meshgrid(lons,lats)
x,y=map(lon,lat)
plt.pcolormesh(x, y, topoin)
levels=[-1000,0,1000]
cs = map.contour(x,y,topoin,levels,linewidths=[1, 2, 1],colors='k')

plt.show()