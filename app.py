import psycopg2
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
from descartes import PolygonPatch
from matplotlib.collections import PatchCollection
from fiona import collection
import fiona
import tkinter as tk
import itertools
from shapely.geometry import Polygon, MultiPolygon, shape
import shapefile

def ret_spec_counts():
    pass

l = []
l2 = []
connection = psycopg2.connect(dbname='dnr_fish', user='postgres', password='Edinburgh.1993', host='localhost')

cursor = connection.cursor()

#cursor.execute('SELECT * FROM dnr_fish LIMIT 500')

#cursor.execute('SELECT common_name, COUNT(*) FROM dnr_fish GROUP BY common_name LIMIT 500')

#l = cursor.fetchall();

#cursor.execute('SELECT column_name FROM information_schema.columns where table_name=%s', ('dnr_fish',))

#l2 = cursor.fetchall()

#print(l)

shps = fiona.open("fom.shp")

#shp = shps['coordinates']
for i in range(10000):
     shp = shps.next()
     if shp['geometry'] != None:
        s = shp['geometry']
        x = s['coordinates']
        print(x[0])
        plt.plot(x[0], x[1], color='red', markersize=3, marker='o')
        #s1 = s['coordinates'].values()
        #print(s1)
#print(s1[1])

plt.grid()
plt.show()


#shp = shps.next()
#shp = shps.next()

#for shp in shps:
#    print(shp['geometry])
#    print('\n')

#for s in shp:
#    print()

#plt.plot(shp)
#plt.show()