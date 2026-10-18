# Каталог анализа фильмов

import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, 
     "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, 
     "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, 
     "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    ratings = [movie['rating'] for movie in movies]
    average = sum(ratings) / len(ratings)
    return round(average, 1)

print(average_rating(movies))

def catalog_age_stats(movies, current_year=2026):
    oldest = min(movies, key=lambda m: m["year"])
    oldest_age = current_year - oldest["year"]
    newset = max(movies, key=lambda m: m["year"])
    newset_age = current_year - newset["year"]
    ages = [current_year - movie["year"] for movie in movies]
    average_age = math.ceil(sum(ages) / len(ages))
    return oldest_age, newset_age, average_age

print(catalog_age_stats(movies))

def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"

print(duration_in_hours(movies[0]["duration_min"]))



def rating_tier(rating):
    if rating >= 9: 
        return "шедевр"  
    elif  rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"

print(rating_tier(9.2))
print(rating_tier(7.3))
print(rating_tier(6.0))
print(rating_tier(4.8))

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _ if year < 2015:
            return "старые"

print(decade_label(2024))   
print(decade_label(2020))   
print(decade_label(2015))   
print(decade_label(2011)) 

for movie in movies:
    if 'comedy' in movie["genres"]:
        continue
    print(movie["title"])


i = 0
while i < len(movies):
    movie = movies[i]
    if movie["rating"] > 9.0:
        print(movie["title"])
        break
    i += 1
else:
    print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count
print(count_long_movies(movies))


def normalize_title(title):
    words = title.split()
    normalized_words = [
        word[0].upper() + word[1:]
        for word in words
    ]
    return ' '.join(normalized_words)

def make_slug(title):
    normalized  = normalize_title(title)
    slug = normalized.lower()
    slug = slug.replace(' ', '-')
    return slug

def format_report_line(movie):
    sorted_genres = sorted(movie['genres'])
    duration = duration_in_hours(movie['duration_min'])
    return (
        f'"{movie["title"]}" '
        f'({movie["year"]}) — '
        f'{movie["rating"]}/10, '
        f'{duration}, '
        f'жанры: {", ".join(sorted_genres)}'
    )
print(normalize_title("silent hours")) 
print(make_slug("Silent Hours"))        
print(format_report_line(movies[7]))    

def titles_sorted_by_rating(movies):
    titles_sorted = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in titles_sorted]

def top_n_by_rating(movies, n=3):
    titles_sorted = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in titles_sorted[:n]]

def count_by_genre(movies):
    counts={}
    for movie in movies:
        for genre in movie ["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts
print(count_by_genre(movies))

def actor_filmography(movies):
    filmography={}
    for movie in movies:
        for actor in movie["actors"]:
            films = filmography.get(actor, [])
            films.append(movie["title"])
            filmography[actor] = films
    return filmography
print(actor_filmography(movies))      

average = average_rating(movies)
above_average = { 
    movie["title"]: movie["rating"] 
    for movie in movies 
    if movie["rating"] > average }
print(above_average)

def all_genres(movies):
    genres = set()
    for movie in movies:
        genres = genres | movie["genres"] 
    return genres
print(all_genres(movies))

def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])
print(common_actors(movies[0], movies[3]))

def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b
print (genres_only_in_one(movies[5:6], movies[:5]))

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

for movie in iter_high_rated(movies):
    print(format_report_line(movie))

total_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)   # 713 
print (total_duration)

def build_report(movies):
    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    stats = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {stats[2]} лет")

    title_to_movie = { movie["title"]: movie for movie in movies }
    print("Топ-3 фильма:")
    for title, _ in top_n_by_rating(movies):
        print(format_report_line(title_to_movie[title]))

    print("Фильмов по жанрам:")
    counts = count_by_genre(movies)
    for genre, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{genre} — {count}")

    print(f"Все жанры каталога: {', '.join(sorted(all_genres(movies)))}")

build_report(movies)