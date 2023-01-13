import sqlite3

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

print(search_title(name_film))