import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import matplotlib.animation as anim
import numpy as np
from postgres_db_methods import init_scatter_and_fetch, inc

x,y=[],[]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
x_init, y_init = init_scatter_and_fetch(x, y)
scat = ax.scatter(x_init, y_init, color='blue', marker='o', s=2, transform=ccrs.Geodetic())
i = 0

def init():
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
    ax.set_extent([-100, -83, 40, 55])
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()

def animate(l, ax, fig, scat):
        global i
        i = i + 1
        plt.title('{}'.format(1889 + i))
        x,y= inc(i)
        scat.set_offsets(np.c_[x, y])

def tour(*args):
    init()
    plt.title('{}'.format(1890))
    animm = anim.FuncAnimation(fig, animate, fargs=(ax, fig, scat), interval=1000, repeat_delay=100)
    plt.show()
    return animm

#tour()