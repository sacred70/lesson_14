import sqlite3

# show_id text
# type text
# title text
# director text
# cast text
# country text
# date_added datetime
# release_year int
# rating text
# duration int
# duration_type text
# listed_in text
# description text

#title_user = input()

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    query = "SELECT title FROM netflix"
    cursor.execute(query)
    print(cursor.fetchall())
    """for row in cursor.fetchall():
        print(row)"""