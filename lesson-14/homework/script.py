 JSON Parsing

📁 students.json (namuna fayl):

[
    {"name": "Ali", "age": 20, "major": "Computer Science"},
    {"name": "Laylo", "age": 22, "major": "Mathematics"},
    {"name": "Otabek", "age": 21, "major": "Physics"}
]


📄 json_parsing.py

import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

🌦️ Weather API

👉 OpenWeather
 API’ga ishlash uchun API kalit kerak bo‘ladi (ro‘yxatdan o‘tib bepul olasiz).

📄 weather.py

import requests

API_KEY = "YOUR_API_KEY"   # bu yerga OpenWeather API kalitingizni yozing
CITY = "Tashkent"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error: Weather data not found")

📚 JSON Modification (Books)

📁 books.json (namuna fayl):

[
    {"title": "Python Basics", "author": "John Doe", "year": 2020},
    {"title": "Data Science Handbook", "author": "Jane Smith", "year": 2019}
]


📄 books_manager.py

import json

FILE = "books.json"

def load_books():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

def add_book(title, author, year):
    books = load_books()
    books.append({"title": title, "author": author, "year": year})
    save_books(books)

def update_book(title, new_data):
    books = load_books()
    for book in books:
        if book["title"] == title:
            book.update(new_data)
    save_books(books)

def delete_book(title):
    books = load_books()
    books = [book for book in books if book["title"] != title]
    save_books(books)

# Test
if __name__ == "__main__":
    add_book("AI Revolution", "Elon Musk", 2025)
    update_book("Python Basics", {"year": 2021})
    delete_book("Data Science Handbook")

    print("Books:", load_books())

🎬 Movie Recommendation System

👉 OMDb API (http://www.omdbapi.com/
) ham API kalit bilan ishlaydi. (Ro‘yxatdan o‘tib apikey olishingiz kerak).

📄 movie_recommender.py

import requests
import random

API_KEY = "YOUR_OMDB_API_KEY"
BASE_URL = "http://www.omdbapi.com/"

def get_movies_by_genre(genre):
    movies = []
    for page in range(1, 3):  # bir nechta sahifa chaqirish
        params = {
            "apikey": API_KEY,
            "s": genre,   # qidiruv
            "type": "movie",
            "page": page
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if "Search" in data:
            movies.extend(data["Search"])
    return movies

if __name__ == "__main__":
    genre = input("Movie genre kiriting (masalan, action, comedy, drama): ")
    movies = get_movies_by_genre(genre)

    if movies:
        movie = random.choice(movies)
        print("Tavsiya qilinadigan film:", movie["Title"], f"({movie['Year']})")
    else:
        print("Hech qanday film topilmadi.")
