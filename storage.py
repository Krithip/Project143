import csv
all_movies = []
with open('C:/Users/Krithi/Desktop/Python/final1.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1]
liked_movie = []
not_liked_movies = []
did_not_watch = []