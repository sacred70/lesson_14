# coding: utf8
import sqlite3
import pprint



#name_film = "Yeh Meri Family"

DB_PATH = 'netflix.db'  # Путь к БД

def cursor_fetchall(db_path, query):
    """ Подключение к БД """
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def search_title(name_movie: str):

    """Реализуйте поиск по названию.
     Если таких фильмов несколько,
     выведите самый свежий."""

    query = f"""SELECT title, country, release_year, listed_in, description 
    FROM netflix 
    WHERE title = '{name_movie}' 
    ORDER BY date_added desc 
    LIMIT 1"""

    result = cursor_fetchall(DB_PATH, query)
    movie_list = [{'title': row[0],
                   'country': row[1],
                   'release_year': row[2],
                   'genre': row[3],
                   'description': row[4]} for row in result]
    return movie_list

#pprint.pprint( search_title(name_film), indent=1)


def search_rating(inquiry):
    """поиск по рейтингу."""
    inquiry = str(inquiry)

    if inquiry == "children":
        query = f"""SELECT description, rating, title  
        FROM netflix 
        WHERE rating = 'G'"""
    elif inquiry == "family":
        query = f"""SELECT description, rating, title  
        FROM netflix 
        WHERE rating = 'G' OR rating = 'PG' OR rating = 'PG-13'"""
    elif inquiry == "adult":
        query = f"""SELECT description, rating, title  
        FROM netflix 
        WHERE rating = 'R' OR rating = 'NC-17'"""
    else:
        return "Такого варианта нет"

    result = cursor_fetchall(DB_PATH, query)
    movie_list = [{'title': row[2],
                   'rating': row[1],
                   'description': row[0]
                   } for row in result]
    return movie_list

#inquiry = "family"
#pprint.pprint(search_rating(inquiry), indent=1)


def search_year(year_from, year_to):
    """поиск по диапазону лет выпуска,
    выводит первые 100 вариантов."""

    query = f"""SELECT title, release_year 
    FROM netflix WHERE release_year 
    BETWEEN {year_from} AND {year_to} 
    LIMIT 100"""
    result = cursor_fetchall(DB_PATH, query)
    movie_list = [{'title': row[0],
                   'release_year': row[1]
                   } for row in result]
    return movie_list


def search_genre(genre):
    """получает название жанра в качестве
    аргумента и возвращает 10 самых свежих фильмов"""

    query = f"""SELECT title, description 
    FROM netflix 
    WHERE listed_in 
    LIKE '%{genre}%' 
    ORDER BY date_added 
    LIMIT 10"""
    result = cursor_fetchall(DB_PATH, query)
    movie_list = [{'title': row[0],
                   'description': row[1]
                   } for row in result]
    return movie_list


def cast_actors(actor_1, actor_2):
    """Задание №5. функция, которая получает в
    качестве аргумента имена двух 
    актеров, сохраняет всех актеров 
    из колонки cast и возвращает список 
    тех, кто играет с ними в паре 
    больше 2 раз."""


    query = f"""SELECT netflix.cast 
        FROM netflix 
        WHERE netflix.cast  
        LIKE '%{actor_1}%' 
        AND netflix.cast  
        LIKE '%{actor_2}%'"""
    all_actors = []
    result = cursor_fetchall(DB_PATH, query)
    for row in result:
        for actors in row:
            all_actors.extend(actors.split(', '))
    count_actors = []
    for actor in all_actors:

        if actor != actor_1 and actor != actor_2:

            if all_actors.count(actor) >= 2:
                count_actors.append(actor)
        else:
            continue

    return count_actors

#actor_1 = "Rose McIver"
#actor_2 = "Ben Lamb"
#pprint.pprint(cast_actors(actor_1, actor_2))


def search_type_yaer_genre(genre, type, yaer):
    """Задание №6. функция, с помощью которой можно будет
    передавать тип картины (фильм или сериал),
    год выпуска и ее жанр и получать на выходе
    список названий картин с их описаниями"""

    query = f"""SELECT title, description 
        FROM netflix 
        WHERE listed_in LIKE '%{genre}%'
        AND type = '{type}'
        AND release_year = {yaer}"""
    result = cursor_fetchall(DB_PATH, query)
    movie_list = [{'title': row[0],
                   'description': row[1]
                   } for row in result]
    return movie_list

#pprint.pprint(search_type_yaer_genre('Dramas', 'Movie', 2000))


