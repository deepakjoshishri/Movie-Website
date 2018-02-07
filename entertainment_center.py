#!/usr/bin/python
# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

# create objects for Movie class available
# in media.py by supplying relavant information

padmaavat = media.Movie(
    'Padmaavat',
    'https://files2.geometria.ru/pics/original/066/261/66261742.jpg',
    'Drama/Action',
    'https://www.youtube.com/watch?v=8YaF2m7hCx0',
    '2h : 44m',
    'Story of how Rani Padmaavati saved the pride of Rajputs.',
    'Sanjay Leela Bhansali',
    'Sanjay Leela Bhansali,Ajit Andhare',
    )

dangal = media.Movie(
    'Dangal',
    'http://www.behindwoods.com/hindi-movies/dangal/stills-photos-pictures/dangal-hd-posters-photos-stills-06.jpg',  # noqa
    'Drama/Sport',
    'https://www.youtube.com/watch?v=x_7YlGv9u1g',
    '2h : 49m',
    'Story of an Indian wrestler.',
    'Nitesh Tiwari',
    'Aamir Khan, Kiran Rao, Siddharth Roy Kapur',
    )

fanaa = media.Movie(
    'Fanaa',
    'http://www.gstatic.com/tv/thumb/movieposters/162198/p162198_p_v8_ac.jpg',
    'Drama/Bollywood',
    'https://www.youtube.com/watch?v=hZk7v4KOTCA',
    '2h : 56m',
    'Love story of an innocent Indian girl and a terrorist.',
    'Kunal Kohli',
    'Yash Chopra',
    )

thor = media.Movie(
    'Thor Ragnarok',
    'https://pre00.deviantart.net/65d1/th/pre/f/2017/166/8/a/8a68ea0511e1062b836871a7a3f9f459-dbct1ki.png',  # noqa
    'Fantasy/Science fiction film',
    'https://www.youtube.com/watch?v=ue80QwXMRHg',
    '2h : 10m',
    'Thor: Ragnarok is a 2017 American superhero film based on the Marvel Comics character Thor.',  # noqa
    'Taika Waititi',
    'Kevin Feige',
    )

jurrasic = media.Movie(
    'Jurassic Park',
    'https://image.tmdb.org/t/p/w500/26L7XODsNlxX3VwkfuUnYOslbRF.jpg',
    'Fantasy/Science fiction',
    'https://www.youtube.com/watch?v=lc0UehYemQA',
    '2h : 7m',
    'During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok.',  # noqa
    'Steven Spielberg',
    'Kathleen Kennedy',
    )

beautifulMind = media.Movie(
    'A Beautiful Mind',
    'http://www.gstatic.com/tv/thumb/movieposters/28869/p28869_p_v8_ad.jpg',
    'Drama/Romance',
    'https://www.youtube.com/watch?v=aS_d0Ayjw4o',
    '2h : 20m',
    'John Nash, a brilliant but asocial mathematical genius, finds himself in pain when he encounters a cruel disorder....',  # noqa
    'Ron Howard',
    'Ron Howard,Brian Grazer',
    )

# create list of movies

movies = [
    dangal,
    fanaa,
    padmaavat,
    jurrasic,
    thor,
    beautifulMind,
    ]

# pass the movies list to fresh tomatoes open_movie_page function

fresh_tomatoes.open_movies_page(movies)
