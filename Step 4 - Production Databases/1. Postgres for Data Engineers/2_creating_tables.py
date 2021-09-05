'''
1.Incorrect Data Types
'''
# query_string = """
#     INSERT INTO ign_reviews VALUES(
#         5249979066121302000, 
#         'Amazing', 
#         'LittleBigPlanet PS Vita', 
#         '/games/littlebigplanet-vita/vita-98907', 
#         'PlayStation Vita', 
#         9.0,
#         'Platformer', 
#         'Y', 
#         2012, 
#         9, 
#         12
#     );
# """

# import psycopg2
# conn = psycopg2.connect("dbname=dq user=dq password=dq")
# cur = conn.cursor()
# cur.execute(query_string)

'''
2.Describing a Table
'''
# import psycopg2
# conn = psycopg2.connect("dbname=dq user=dq password=dq")
# cur = conn.cursor()
# cur.execute("SELECT * FROM ign_reviews LIMIT 0;")
# print(cur.description)
# conn.close()

'''
3.Understanding the Description
'''
# import psycopg2
# conn = psycopg2.connect("dbname=dq user=dq password=dq")
# cur = conn.cursor()
# cur.execute("SELECT typname FROM pg_catalog.pg_type WHERE oid = 25;")
# type_name_25 = cur.fetchone()[0]
# print(type_name_25)
# cur.execute("SELECT typname FROM pg_catalog.pg_type WHERE oid = 700;")
# type_name_700 = cur.fetchone()[0]
# print(type_name_700)

'''
4.Finding the Right id Data Type
'''
# import psycopg2
# conn = psycopg2.connect("dbname=dq user=dq password=dq")
# cur = conn.cursor()
# cur.execute("""
# ALTER TABLE ign_reviews
# ALTER COLUMN id TYPE bigint
# """)
# conn.commit()
# conn.close()

'''
5.Float-like Types
'''

