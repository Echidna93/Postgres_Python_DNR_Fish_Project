import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from fiona import collection
import fiona
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from pyproj import Proj, transform as tran

shps = fiona.open("fom.shp")

ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cfeat.COASTLINE)
ax.add_feature(cfeat.LAND)
ax.add_feature(cfeat.OCEAN)

stateborders = cfeat.NaturalEarthFeature(category='cultural',
                                    name='admin_1_states_provinces_lines',
                                    scale='10m',
                                    facecolor='none')
intlborders = cfeat.NaturalEarthFeature(category='cultural',
                                    name='admin_0_countries',
                                    scale='50m',
                                    facecolor='none')

ax.add_feature(stateborders, edgecolor='black')
ax.add_feature(intlborders, edgecolor='black')
#ax.add_feature(details)
ax.add_feature(cfeat.LAND)
ax.add_feature(cfeat.COASTLINE)
ax.add_feature(cfeat.LAKES)
ax.add_feature(cfeat.OCEAN)
ax.add_feature(cfeat.RIVERS)

for i in range(300):
     shp = shps.next()
     if shp['geometry'] != None:
        s = shp['geometry']
        x = s['coordinates']
        inProj = Proj(init='epsg:26715')
        outProj = Proj(init='epsg:4326')
        x2, y2 = tran(inProj, outProj, x[0], x[1])
        plt.plot(x2, y2, marker='o', transform=ccrs.Geodetic())

ax.set_extent([-100, -85, 40, 55])
plt.show()