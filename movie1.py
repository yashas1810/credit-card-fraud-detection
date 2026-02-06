movies = {
    "1": 200,
    "2": 180,
    "3": 220,
    "4": 150
}

name = input("Enter name: ")
movie = input("Enter movie: ").title()

if movie in movies:
    tickets = int(input("Enter tickets: "))
    total = tickets * movies[movie]

    with open("movietext.txt", "a", encoding="utf-8") as f:
        f.write(f"{name}, {movie}, {tickets}, {total}\n")
        print("booking saved")
else:
    print("booking not saved")


