#!/usr/bin/python

import psycopg2
import sys

conn = psycopg2.connect(database="mahipal", user = "mahipal", password = "mahipal04", host = "127.0.0.1", port = "5432")

print "Opened database successfully"
cur = conn.cursor()

#Cannot execute a query when passed authorname as an commandline args
#cmdargs = sys.argv[1]
#print "Author name : ", cmdargs
#cur.execute("SELECT all bookname from books as a, author as b where a.authorid=b.authorid and b.authorid in(select authorid from author where authorname = +cmdargs)")
cur.execute("SELECT all bookname from books as a, author as b where a.authorid=b.authorid and b.authorid in(select authorid from author where authorname = 'Paul')")
rows = cur.fetchall()
for row in rows:
   print "BOOKS = ", row


print "Operation done successfully";
conn.close()