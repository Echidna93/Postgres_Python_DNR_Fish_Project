import psycopg2
from pyproj import Proj, transform as tran



connection = psycopg2.connect(dbname='dnr_fish', user='postgres', password='Edinburgh**1993', host='localhost')
cursor = connection.cursor()

def init_scatter_and_fetch(x, y):
    sql = "SELECT utm_x, utm_y FROM dnr_fish WHERE EXTRACT(year FROM date_caught)=1890;"
    cursor.execute(sql)
    b = cursor.fetchall()
    inProj = Proj(init='epsg:26715')
    outProj = Proj(init='epsg:4326')
    for a in range(len(b)):
        x2n, y2n = tran(inProj, outProj, b[a][0], b[a][1])
        x.append(x2n)
        y.append(y2n)
    return x, y

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
