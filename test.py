import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from fiona import collection
import psycopg2
import fiona
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from pyproj import Proj, transform as tran
import matplotlib.animation as anim
from matplotlib.animation import FuncAnimation


connection = psycopg2.connect(dbname='dnr_fish', user='postgres', password='Edinburgh**1993', host='localhost')
cursor = connection.cursor()

i = 0
startyear: int = 1890

def load_data_from_dict():
    for i in range(300):
         shp = shps.next()
         if shp['geometry'] != None:
            s = shp['geometry']
            x = s['coordinates']
            inProj = Proj(init='epsg:26715')
            outProj = Proj(init='epsg:4326')
            x2, y2 = tran(inProj, outProj, x[0], x[1])
            plt.plot(x2, y2, marker='o', transform=ccrs.Geodetic())

shps = fiona.open("fom.shp")

def inc(i):
    sql = "SELECT utm_x, utm_y FROM dnr_fish WHERE EXTRACT(year FROM date_caught)={};".format(1960+i)
    cursor.execute(sql)
    b = cursor.fetchall()
    x2=[]
    y2=[]
    inProj = Proj(init='epsg:26715')
    outProj = Proj(init='epsg:4326')
    for a in range(len(b)):
        x2n, y2n = tran(inProj, outProj, b[a][0], b[a][1])
        x2.append(x2n)
        y2.append(y2n)
    return x2, y2

def animate(l, ax, fig):
        ax.cla()
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
        # ax.add_feature(details)
        ax.add_feature(cfeat.LAND)
        ax.add_feature(cfeat.COASTLINE)
        ax.add_feature(cfeat.LAKES)
        ax.add_feature(cfeat.OCEAN)
        plt.title('stuff')
        ax.add_feature(cfeat.RIVERS)
        ax.set_extent([-100, -85, 40, 55])

        global i
        i = i + 1
        y2 = []
        x2 , y2 = inc(i)
        print(x2, y2)
        plt.scatter(x2, y2, color='blue', marker='o', s=2, transform=ccrs.Geodetic())
        #fig.canvas.flush_events()
        #i = i+1

#animate()

def main():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
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
    # ax.add_feature(details)
    ax.add_feature(cfeat.LAND)
    ax.add_feature(cfeat.COASTLINE)
    ax.add_feature(cfeat.LAKES)
    ax.add_feature(cfeat.OCEAN)
    ax.add_feature(cfeat.RIVERS)
    ax.set_extent([-100, -85, 40, 55])
    animm = anim.FuncAnimation(fig, animate, 2, fargs=(ax, fig), interval=1000, repeat_delay=100)
    plt.show()
    return animm

main()