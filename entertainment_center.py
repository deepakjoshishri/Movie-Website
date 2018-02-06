import media
import fresh_tomatoes

#create objects for Movie class available in media.py by supplying relavant information

padmaavat = media.Movie("Padmaavat","https://files2.geometria.ru/pics/original/066/261/66261742.jpg","historic","https://www.youtube.com/watch?v=8YaF2m7hCx0","2h : 44m",
                        "story of how Rani Padmaavati saved the pride of Rajputs","Sanjay Leela Bhansali","Sanjay Leela Bhansali,Ajit Andhare");

movies = [padmaavat]

fresh_tomatoes.open_movies_page(movies)
