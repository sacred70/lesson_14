import sqlite3
import pprint

name_film = "Yeh Meri Family"

DB_PATH = 'netflix.db'  # Путь к БД

def cursor_fetchall(db_path, query):
    """ Подключение к БД """
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def search_title(name_film:str):
    """Реализуйте поиск по названию.
     Если таких фильмов несколько,
     выведите самый свежий."""


    query = f"""SELECT title, country, release_year, listed_in, description FROM netflix WHERE title = '{name_film}' ORDER BY date_added desc LIMIT 1"""

    result = cursor_fetchall(DB_PATH, query)
    movie_list = [{'title': row[0],
                   'country': row[1],
                   'release_year': row[2],
                   'genre': row[3],
                   'description': row[4]} for row in result]
    return movie_list

#pprint.pprint( search_title(name_film), indent=1)


def search_year(release_year):
    """поиск по диапазону лет выпуска,
    выводит первые 100 вариантов."""

    query = f"""SELECT title, release_year FROM netflix WHERE release_year = '{release_year}' ORDER BY release_year desc LIMIT 100"""
    result = cursor_fetchall(DB_PATH, query)
    movie_list = [{'release_year': row[1],
                   'title': row[0]
                   } for row in result]
    return movie_list

release_year = 1995
#pprint.pprint(search_year(release_year), indent=1)
