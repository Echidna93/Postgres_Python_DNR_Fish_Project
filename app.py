import psycopg2


l = []
l2 = []
connection = psycopg2.connect(dbname='DNR_FISH', user='postgres', password='Edinburgh.1993', host='localhost')

cursor = connection.cursor()

cursor.execute('SELECT * FROM dnr_fish LIMIT 1')

l = cursor.fetchone()

cursor.execute('SELECT column_name FROM information_schema.columns where table_name=%s', ('dnr_fish',))

l2 = cursor.fetchall()

print(l)
print(l2)
