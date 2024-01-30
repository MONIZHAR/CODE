import json

MOVIE_FILE = "movies.json"

def load_movies():
    try:
        with open(MOVIE_FILE, 'r') as file:
            movies = json.load(file)
    except FileNotFoundError:
        movies = []
    return movies

def save_movies(movies):
    with open(MOVIE_FILE, 'w') as file:
        json.dump(movies, file, indent=2)

def show_all_movies():
    movies = load_movies()
    if not movies:
        print("No movies found.")
    else:
        for movie in movies:
            print(movie)

def add_new_movie():
    director = input("Enter director: ")
    release_year = input("Enter release year: ")
    language = input("Enter language: ")
    rating = input("Enter rating: ")

    movie = {
        "Director": director,
        "Release Year": release_year,
        "Language": language,
        "Rating": rating
    }

    movies = load_movies()
    movies.append(movie)
    save_movies(movies)
    print("Movie added successfully.")

def filter_movies(criteria, value):
    movies = load_movies()
    filtered_movies = [movie for movie in movies if movie[criteria] == value]
    return filtered_movies

def search_for_movie():
    name = input("Enter the name of the movie to search: ")
    movies = load_movies()
    for movie in movies:
        if movie["Name"].lower() == name.lower():
            print(movie)
            return
    print("Movie not found.")

def update_movie_details():
    name = input("Enter the name of the movie to update: ")
    movies = load_movies()
    for movie in movies:
        if movie["Name"].lower() == name.lower():
            director = input("Enter new director: ")
            release_year = input("Enter new release year: ")
            language = input("Enter new language: ")
            rating = input("Enter new rating: ")

            movie["Director"] = director
            movie["Release Year"] = release_year
            movie["Language"] = language
            movie["Rating"] = rating

            save_movies(movies)
            print("Movie details updated successfully.")
            return
    print("Movie not found.")

def delete_movie():
    name = input("Enter the name of the movie to delete: ")
    movies = load_movies()
    for movie in movies:
        if movie["Name"].lower() == name.lower():
            movies.remove(movie)
            save_movies(movies)
            print("Movie deleted successfully.")
            return
    print("Movie not found.")

def filter_movies_by_criteria():
    print("Filter movies by:")
    print("1. Name\n2. Director\n3. Release Year\n4. Language\n5. Rating")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        value = input("Enter name: ")
        return filter_movies("Name", value)
    elif choice == "2":
        value = input("Enter director: ")
        return filter_movies("Director", value)
    elif choice == "3":
        value = input("Enter release year: ")
        return filter_movies("Release Year", value)
    elif choice == "4":
        value = input("Enter language: ")
        return filter_movies("Language", value)
    elif choice == "5":
        value = input("Enter rating: ")
        return filter_movies("Rating", value)
    else:
        print("Invalid choice.")
        return []

def get_number_of_movies_in_language():
    language = input("Enter the language to count movies for: ")
    movies = load_movies()
    count = sum(1 for movie in movies if movie["Language"].lower() == language.lower())
    print(f"Number of movies in {language}: {count}")

def main():
    while True:
        print("\nMovie List Application\n")
        print("1. Show all Movies")
        print("2. Add a New Movie")
        print("3. Filter Movies based on criteria")
        print("4. Search for a Movie")
        print("5. Update a Movie's Details")
        print("6. Delete a Movie")
        print("7. Get Number of Movies in a Specified Language")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == "1":
            show_all_movies()
        elif choice == "2":
            add_new_movie()
        elif choice == "3":
            filtered_movies = filter_movies_by_criteria()
            for movie in filtered_movies:
                print(movie)
        elif choice == "4":
            search_for_movie()
        elif choice == "5":
            update_movie_details()
        elif choice == "6":
            delete_movie()
        elif choice == "7":
            get_number_of_movies_in_language()
        elif choice == "8":
            print("Exiting Movie List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
