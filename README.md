Firstly created a database in postgresql manually.
CREATE DATABASE <database_name> e.g CREATE DATABASE mydb
After successuflly creating database then execute models.py (this script make a connection and create two table: author and books)
After making connection we can insert raw-data on both the tables through executing insert_author.py and insert_book.py
Now in final step to get books name for a specified author when execute function_module.py (currently in this commit we pass author name hardcoded in query instead of command line argrument).
Follow above steps properly.
