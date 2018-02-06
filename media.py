#!/usr/bin/python
# -*- coding: utf-8 -*-

# Parent class


class Media:

    """ This class provides a way to store generic information related to media"""

    # documentation for base class

    def __init__(self, title, poster_image, genre, trailer_youtube):
        self.title = title
        self.poster_image_url = poster_image
        self.genre = genre
        self.trailer_youtube_url = trailer_youtube


# Child class of Media

class Movie(Media):

    """ This is an extenion of Media class that stores information related to movies specifically"""

    # documentation for child class which inherits attributes of Media class as parent

    # Constructor for child class

    def __init__(self, title, poster_image, genre, youtube_trailer, duration, storyline, director, producer):
        super().__init__(title, poster_image, genre, youtube_trailer)  # Calling parent class constructor
        self.duration = duration
        self.storyline = storyline
        self.director = director
        self.producer = producer


# Child class of Movie

class Anime(Movie):

    """ This is an extenion of Media class that stores information related to movies specifically"""

    # documentation for child class which inherits attributes of My class as parent

    # Constructor for child class

    def __init__(self, title, poster_image, genre, youtube_trailer, duration, storyline, director, producer, no_of_seasons, importat_characters):
        super().__init__(  # Calling Base class constructor
            title,
            poster_image,
            genre,
            youtube_trailer,
            duration,
            storyline,
            director,
            producer,
            )
        self.no_of_episodes = no_of_episodes
        self.important_characters = important_characters


# Child class of Media

class TVShows(Media):

    """ This is an extenion of Media class that stores information related to movies specifically"""

    # documentation for child class which inherits attributes of Media class as parent

    # Constructor for child class

    def __init__(self, title, poster_image, genre, youtube_trailer, no_of_episodes, storyline, director, producer):
        super().__init__(title, poster_image, genre, youtube_trailer)  # Calling Base class constructor
        self.no_of_episodes = no_of_episodes
