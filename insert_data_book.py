#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="mahipal", user = "mahipal", password = "mahipal04", host = "127.0.0.1", port = "5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("INSERT INTO BOOKS (BOOKID,AUTHORID,BOOKNAME) \
      VALUES (11, 1, 'C LANGUAGE')");

cur.execute("INSERT INTO BOOKS (BOOKID,AUTHORID,BOOKNAME) \
      VALUES (12, 1, 'PYTHON')");

cur.execute("INSERT INTO BOOKS (BOOKID,AUTHORID,BOOKNAME) \
      VALUES (13, 1, 'ADA')");

cur.execute("INSERT INTO BOOKS (BOOKID,AUTHORID,BOOKNAME) \
      VALUES (14, 2, 'C++ BOOK')");

cur.execute("INSERT INTO BOOKS (BOOKID,AUTHORID,BOOKNAME) \
      VALUES (15, 2, 'C# BOOK')");
	  
cur.execute("INSERT INTO BOOKS (BOOKID,AUTHORID,BOOKNAME) \
      VALUES (16, 3, 'HALF GIRLFRIEND')");
	  
cur.execute("INSERT INTO BOOKS (BOOKID,AUTHORID,BOOKNAME) \
      VALUES (17, 3, 'FULL MOON')");
	  
cur.execute("INSERT INTO BOOKS (BOOKID,AUTHORID,BOOKNAME) \
      VALUES (18, 4, 'NIGHTANGLE')");

conn.commit()
print "Records created successfully";
conn.close()