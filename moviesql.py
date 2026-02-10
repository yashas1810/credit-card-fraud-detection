import mysql.connector

# Step 1: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # replace if needed
    password="root",      # replace if needed
    database="yashas"
)
cursor = conn.cursor()

# Step 2: Create table (run once)
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150),
    genre VARCHAR(50),
    release_year INT,
    rating FLOAT
)
""")
conn.commit()

# Step 3: Functions for CRUD
def add_movie(title, genre, release_year, rating):
    cursor.execute(
        "INSERT INTO movies (title, genre, release_year, rating) VALUES (%s, %s, %s, %s)",
        (title, genre, release_year, rating)
    )
    conn.commit()
    print("Movie added!")

def view_movies():
    cursor.execute("SELECT * FROM movies")
    for row in cursor.fetchall():
        print(row)

def update_movie(movie_id, new_rating):
    cursor.execute(
        "UPDATE movies SET rating=%s WHERE id=%s",
        (new_rating, movie_id)
    )
    conn.commit()
    print("Movie updated!")

def delete_movie(movie_id):
    cursor.execute(
        "DELETE FROM movies WHERE id=%s",
        (movie_id,)
    )
    conn.commit()
    print("Movie deleted!")

# Step 4: Menu-driven program
while True:
    print("\n--- Movie Management ---")
    print("1. Add Movie")
    print("2. View Movies")
    print("3. Update Movie Rating")
    print("4. Delete Movie")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter movie title: ")
        genre = input("Enter genre: ")
        release_year = int(input("Enter release year: "))
        rating = float(input("Enter rating (0–10): "))
        add_movie(title, genre, release_year, rating)

    elif choice == "2":
        view_movies()

    elif choice == "3":
        movie_id = int(input("Enter movie ID: "))
        new_rating = float(input("Enter new rating: "))
        update_movie(movie_id, new_rating)

    elif choice == "4":
        movie_id = int(input("Enter movie ID: "))
        delete_movie(movie_id)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")

# Close connection
cursor.close()
conn.close()
