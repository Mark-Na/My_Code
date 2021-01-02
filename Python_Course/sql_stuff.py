# import psycopg2 as pg2
# secret = 'S0ju1sBOMb'
# conn = pg2.connect(database = 'dvdrental',user = 'postgres',password = secret )
# cur = conn.cursor()
# cur.execute('SELECT * FROM payment')
# data = (cur.fetchmany(10))
# print(data[0][4])
# conn.close()

# import sqlite3
# conn = sqlite3.connect("my_friends.db")
# # create cursor object
# c = conn.cursor()
# #execute some sql
# #c.execute("CREATE TABLE friends (first_name TEXT,last_name TEXT, closeness INTEGER);")
# insert_query = ''' INSERT INTO friends VALUES('Merriweather' , 'Lewis', 7)'''
# c.execute(insert_query)
# # commit changes
# conn.commit()
# conn.close()

# #set PATH=%PATH%;C:\sqlite;

#' OR 1==1-- is example of SQL injection
# "SELECT * FROM users WHERE username = ? AND password = ?"
# c.execute(query(u,p))