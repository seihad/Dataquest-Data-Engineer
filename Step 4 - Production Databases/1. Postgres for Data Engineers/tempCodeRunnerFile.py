from datetime import date
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq password=dq")
cur = conn.cursor()
game_data = (52499790661213, 'Amazing', 'LittleBigPlanet PS Vita', '/games/littlebigplanet-vita/vita-98907', 'PlayStation Vita', 9.0, 'Platformer', 'y', date(2012, 12, 9))
mogrified_values = cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", game_data)
conn_encoding = conn.encoding
game_data = cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", game_data)
mogrified_values_decoded = game_data.decode(conn_encoding)
print(conn_encoding)
print(mogrified_values_decoded)
