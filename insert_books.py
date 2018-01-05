#import os
#import sys
#import psycopg2
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import PrimaryKeyConstraint
 
Base = declarative_base()

class Books(Base):
	__tablename__ = 'books'
	bookid = Column(Integer, primary_key=True)
	bookname = Column(String(50))
	authorid = Column(Integer, ForeignKey('author.authorid'), primary_key=True)
	author = relationship('Author', backref = 'books')
	
	
class Author(Base):
	__tablename__ = 'author'
	authorid = Column(Integer, primary_key=True)
	authorname = Column(String(50), nullable=False)
	

#os.system("python sqlalchemy_declarative.py")

engine = create_engine('postgresql://mahipalbisht:mahipal04@localhost/mydb')

Base.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()

book1 = Books(bookid = 1, bookname = "C", authorid = 1)
session.add(book1)
session.commit()

book15 = Books(bookid = 1, bookname = "C", authorid = 2)
session.add(book15)
session.commit()


book2 = Books(bookid = 2, bookname = "C++", authorid = 1)
session.add(book2)
session.commit()

book3 = Books(bookid = 3, bookname = "PYTHON", authorid = 1)
session.add(book3)
session.commit()

book4 = Books(bookid = 4, bookname = "JAVA PROGRAMMING", authorid = 1)
session.add(book4)
session.commit()

book5 = Books(bookid = 5, bookname = "HALF GIRLFRIEND", authorid = 2)
session.add(book5)
session.commit()

book6 = Books(bookid = 6, bookname = "ENGLISH SPEAKING", authorid = 2)
session.add(book6)
session.commit()

book7 = Books(bookid = 7, bookname = "ALGORITHMS", authorid = 2)
session.add(book7)
session.commit()

book8 = Books(bookid = 8, bookname = "GRAPHICS", authorid = 3)
session.add(book8)
session.commit()

book9 = Books(bookid = 9, bookname = "DATA STRUCTURE", authorid = 3)
session.add(book9)
session.commit()

book10 = Books(bookid = 10, bookname = "DATABASE", authorid = 4)
session.add(book10)
session.commit()

book11 = Books(bookid = 11, bookname = "SOFTWARE ENGINEERING", authorid = 4)
session.add(book11)
session.commit()

book12 = Books(bookid = 12, bookname = "MATHEMATICS", authorid = 5)
session.add(book12)
session.commit()

book13 = Books(bookid = 13, bookname = "HINDI", authorid = 5)
session.add(book13)
session.commit()

book14 = Books(bookid = 14, bookname = "C IN DEPTH", authorid = 6)
session.add(book14)
session.commit()

