Firstly created a database in postgresql manually.
CREATE DATABASE <database_name> e.g CREATE DATABASE Mahipal
After successuflly creating database then execute connect.py (this script make a connection and create two table: author and books)
After making connction we can insert raw-data on both the tables through executing insert_data_author.py and insert_data_book.py
Now in final step to get books name for a specified author when execute select_data.py (currently in this commit we pass author name hardcoded in query instead of command line argrument).
Follow above steps properly.
