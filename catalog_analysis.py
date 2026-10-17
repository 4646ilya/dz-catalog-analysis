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
