import sqlite3
from flask import Flask, render_template
from function import search_title
from function import search_year


app = Flask(__name__)


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

@app.route("/movie/<title>")
def search_name(title):
    return search_title(title)


@app.route("/movie/year/to/<int:year>")
def search_release_year(year):
    return search_year(year)




app.run()
