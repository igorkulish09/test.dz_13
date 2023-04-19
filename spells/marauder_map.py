from dz_13 import films_titles
from dz_13 import films_awards


class MapMagic:
    def __init__(self):
        self._map_open = "I solemnly swear that I am up to no good."
        self._map_close = "Mischief managed."

    def get_map_open(self):
        return self._map_open

    def get_map_close(self):
        return self._map_close


map_magic = MapMagic()
print(map_magic.get_map_open()) # виведе: "I solemnly swear that I am up to no good."
print(map_magic.get_map_close()) # виведе: "Mischief managed."

class MarauderMap(map_magic):
    _films_titles = {
        "results": [
            {
                "imdb_id": "tt1201607",
                "title": "Harry Potter and the Deathly Hallows: Part 2"
            },
            {
                "imdb_id": "tt0241527",
                "title": "Harry Potter and the Sorcerer's Stone"
            },
            {
                "imdb_id": "tt0926084",
                "title": "Harry Potter and the Deathly Hallows: Part 1"
            },
            {
                "imdb_id": "tt0304141",
                "title": "Harry Potter and the Prisoner of Azkaban"
            },
            {
                "imdb_id": "tt0417741",
                "title": "Harry Potter and the Half-Blood Prince"
            },
            {
                "imdb_id": "tt0295297",
                "title": "Harry Potter and the Chamber of Secrets"
            },
            {
                "imdb_id": "tt0330373",
                "title": "Harry Potter and the Goblet of Fire"
            },
            {
                "imdb_id": "tt0373889",
                "title": "Harry Potter and the Order of the Phoenix"
            }
        ]
    }

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_films_titles():
        return MarauderMap._films_titles

print(MarauderMap.get_films_titles()) # виведе словник з назвами фільмів про Гаррі Поттера

class MarauderMap(MapMagic):
    _films_titles = {
        "results": [
            {
                "imdb_id": "tt1201607",
                "title": "Harry Potter and the Deathly Hallows: Part 2"
            },
            {
                "imdb_id": "tt0241527",
                "title": "Harry Potter and the Sorcerer's Stone"
            },
            {
                "imdb_id": "tt0926084",
                "title": "Harry Potter and the Deathly Hallows: Part 1"
            },
            {
                "imdb_id": "tt0304141",
                "title": "Harry Potter and the Prisoner of Azkaban"
            },
            {
                "imdb_id": "tt0417741",
                "title": "Harry Potter and the Half-Blood Prince"
            },
            {
                "imdb_id": "tt0295297",
                "title": "Harry Potter and the Chamber of Secrets"
            },
            {
                "imdb_id": "tt0330373",
                "title": "Harry Potter and the Goblet of Fire"
            },
            {
                "imdb_id": "tt0373889",
                "title": "Harry Potter and the Order of the Phoenix"
            }
        ]
    }

    def __init__(self, path):
        super().__init__()
        self.path = path

my_map = MarauderMap('path/to/films_awards.json')

import json

class MarauderMap:
    def __init__(self, path):
        self.path = path

    def map_generator(self):
        # виводимо значення map_open скласу MapMagic
        print(MapMagic.map_open)

        # зчитуємо словник з файлу
        with open(self.path) as f:
            films_awards = json.load(f)

        # генеруємо структуру з нагородами
        for result in films_awards[0]['results']:
            movie_title = result['movie']['title']
            event_name = result['event_name']
            award_name = result['award_name']
            year = result['year']
            award = result['award']
            print(f'{movie_title} ({year}): {award_name} - {award} ({event_name})')

        # генеруємо прощання з атрибуту map_close класу MapMagic
        print(MapMagic.map_close)


        marauder_map = MarauderMap("films_awards.json")
        marauder_map.map_generator()