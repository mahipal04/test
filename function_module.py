
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



rows = engine.execute("SELECT bookname from books as a, author as b where a.authorid=b.authorid and b.authorid in(select authorid from author where authorname = 'paul')")

for row in rows:
   print row

