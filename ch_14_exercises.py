"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""
import sqlite3

# TODO 14.1 - 14.3 Opening a database connection with SQLite
print("=" * 10, "Section 14.1-14.3 opening a database connection", "=" * 10)
# establish a connection to an SQL database named dogs.db using dogs_connection as a variable
# Note: A new database should be created if it does not yet exist
my_db = sqlite3.connect('dogs.db')
# create a cursor for working with your database named dogs_cursor
my_dogs = my_db.cursor()
# NOTE: the following statement will delete the Dogs table if it exists
# This statement is included for testing purposes to ensure a clean slate
# each time you re-run your program (remove the # )
# dogs_cursor.execute("""DROP TABLE IF EXISTS Dogs""")
my_dogs.execute("""Drop If Exists Dogs""")

# TODO 14.4 Creating a Table
print("=" * 10, "Section 14.4 creating a table", "=" * 10)
# the following variable will be used in your execute command
table_structure = """CREATE TABLE IF NOT EXISTS Dogs 
                  (DogID INTEGER PRIMARY KEY NOT NULL, 
                  DogName TEXT, OwnerName TEXT, Breed TEXT)"""
# use the cursor variable to execute the SQL command in table_structure
my_dogs.execute(table_structure)
# commit the changes using the database connection variable dogs_connection
my_db.commit()

# TODO 14.5 Adding data to a table
print("=" * 10, "Section 14.5 adding data to a table", "=" * 10)
# complete the following statement to add a total of four records to the table
# the first record has been added for you (remove the # from each line)
my_dogs.execute("""INSERT INTO Dogs (DogName, OwnerName, Breed)
                   VALUES ("Donovan", "Ben", "Golden Retriever"),
                    """)


# commit your changes to make them visible to other database users
my_db.commit()

# TODO 14.6 Querying data with SELECT
print("=" * 10, "Section 14.6 querying data with SELECT", "=" * 10)
# write an execute statement to select all columns (fields) from the Dogs table
my_dogs.execute('Select from')
# fetch all of the results into a list variable
pups = my_dogs.fetchall()
# use a for loop to display the results
for puppy in pups:
    print(puppy)

# TODO 14.6-14.7 updating specific records
print("=" * 10, "Section 14.6-14.7 updating specific records", "=" * 10)
# add a WHERE clause to the following statement to select the dog with DogID 2
# (remove the # to test)
# dogs_cursor.execute("""SELECT * FROM Dogs""")
my_dogs.execute('Select From Dog ID')
# fetch and display the record found
print(my_dogs.fetchone())
# write an execute statement to update the record with DogID 2 to have OwnerName "Unknown"
my_dogs.execute('Select From ID 2')
# Select, fetch and display the updated record with DogID 2
my_dogs.execute('Select * From Dog ID 3')
print(my_dogs.fetchone())
# commit your changes (changes are only visible to your program until committed)
my_db.commit()
# close your connection to the database
my_db.close()