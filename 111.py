import sqlite3
from flask import Flask, render_template
#from search_title.app import search_title_blueprint
from function import search_title

app = Flask(__name__)
#app.register_blueprint(search_title_blueprint)



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
"""
with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    query = "SELECT title FROM netflix"
    cursor.execute(query)
    print(cursor.fetchall())
    """
@app.route ("/movie/<str:title>")
def search(title):
    return search_title(title)


app.run()

