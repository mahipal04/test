#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="mahipal", user = "mahipal", password = "mahipal04", host = "127.0.0.1", port = "5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("INSERT INTO AUTHOR (AUTHORID,AUTHORNAME) \
      VALUES (1, 'Paul')");

cur.execute("INSERT INTO AUTHOR (AUTHORID,AUTHORNAME) \
      VALUES (2, 'Allen')");

cur.execute("INSERT INTO AUTHOR (AUTHORID,AUTHORNAME) \
      VALUES (3, 'Teddy')");

cur.execute("INSERT INTO AUTHOR (AUTHORID,AUTHORNAME) \
      VALUES (4, 'Mark')");

conn.commit()
print "Records created successfully";
conn.close()