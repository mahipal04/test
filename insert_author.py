
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
	
engine = create_engine('postgresql://mahipalbisht:mahipal04@localhost/mydb')

Base.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()

author1 = Author(authorid = 1, authorname = "paul")
session.add(author1)
session.commit()

author2 = Author(authorid = 2, authorname = "harshad")
session.add(author2)
session.commit()

author3 = Author(authorid = 3, authorname = "arjun")
session.add(author3)
session.commit()
author4 = Author(authorid = 4, authorname = "kapil")
session.add(author4)
session.commit()
author5 = Author(authorid = 5, authorname = "kunal")
session.add(author5)
session.commit()
author6 = Author(authorid = 6, authorname = "mahipal")
session.add(author6)
session.commit()

