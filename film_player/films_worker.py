import os

# Створення директорії film_storage
os.makedirs('film_player/film_storage')

# Створення директорій від A до Z
for letter in range(ord('A'), ord('Z')+1):
    os.makedirs(f'film_player/film_storage/{chr(letter)}')


class Film:
    def __init__(self, title, description, director, writer, cast, running_time, country, language, imdb_rating, year,
                 budget, box_office, is_profitable, is_oscar_nominated, is_oscar_win, trailer):
        self.title = title
        self.description = description
        self.director = director
        self.writer = writer
        self.cast = cast
        self.running_time = running_time
        self.country = country
        self.language = language
        self.imdb_rating = imdb_rating
        self.year = year
        self.budget = budget
        self.box_office = box_office
        self.is_profitable = is_profitable
        self.is_oscar_nominated = is_oscar_nominated
        self.is_oscar_win = is_oscar_win
        self.trailer = trailer

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_director(self):
        return self.director

    def get_writer(self):
        return self.writer

    def get_cast(self):
        return self.cast

    def get_running_time(self):
        return self.running_time

    def get_country(self):
        return self.country

    def get_language(self):
        return self.language

    def get_imdb_rating(self):
        return self.imdb_rating

    def get_year(self):
        return self.year

    def get_budget(self):
        return self.budget

    def get_box_office(self):
        return self.box_office

    def is_profitable(self):
        return self.is_profitable

    def is_oscar_nominated(self):
        return self.is_oscar_nominated

    def is_oscar_win(self):
        return self.is_oscar_win

    def get_trailer(self):
        return self.trailer


class Film:
    def __init__(self, title, description, director, writer, cast, running_time, country, language, imdb_rating, year,
                 budget, box_office, profitable, oscar_nominated, oscar_win, trailer):
        self.title = title
        self.description = description
        self.director = director
        self.writer = writer
        self.cast = cast
        self.running_time = running_time
        self.country = country
        self.language = language
        self.imdb_rating = imdb_rating
        self.year = year
        self.budget = budget
        self.box_office = box_office
        self.profitable = profitable
        self.oscar_nominated = oscar_nominated
        self.oscar_win = oscar_win
        self.trailer = trailer
        self.storage_address = f"film_storage/{title[0].upper()}/{title.replace(' ', '_')}.txt"

    def upload_file(self):
        with open(self.storage_address, "w") as file:
            file.write(self.description)

    def get_film_address(self):
        return self.storage_address

film = Film("Crazy, Stupid, Love.", "A middle-aged husband's life changes dramatically when his wife asks him for a divorce. He seeks to rediscover his manhood with the help of a newfound friend, Jacob, learning to pick up girls at bars.", ["Glenn Ficarra", "John Requa"], "Dan Fogelman", ["Steve Carell", "Ryan Gosling", "Julianne Moore"], "118 minutes", "United States", "English", 7.4, 2011, "$50 million", "$145 million", True, False, False, "https://www.imdb.com/video/vi3722091801/")
film.upload_file()
print(film.get_film_address())
