#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="mahipal", user = "mahipal", password = "mahipal04", host = "127.0.0.1", port = "5432")

print "Opened database successfully"
cur = conn.cursor()
cur.execute('''CREATE TABLE AUTHOR
      (AUTHORID INT PRIMARY KEY     NOT NULL,
      AUTHORNAME           TEXT    NOT NULL);''')

cur.execute('''CREATE TABLE BOOKS
      (BOOKID INT      NOT NULL,
	  AUTHORID INT  NOT NULL,
      BOOKNAME           CHAR(50)    NOT NULL,
	  PRIMARY KEY(BOOKID),
	  FOREIGN KEY (AUTHORID)
                REFERENCES AUTHOR (AUTHORID)
                ON UPDATE CASCADE ON DELETE CASCADE
	  );''')
	  

print "Table created successfully"

conn.commit()
conn.close()