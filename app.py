from pymongo import MongoClient

# Connect MongoDB Compass local database
client = MongoClient("mongodb://localhost:27017/")

# Database
db = client["Movie_review"]

# Collections
users = db["user_data"]
movies = db["movie_data"]
reviews = db["reviews_data"]

print("Connected to MongoDB")

# Fetch all movies
print("\nMovies List:")
for movie in movies.find():
    print(movie)

# Fetch reviews with movie and user info
print("\nReviews:")

for review in reviews.find():

    movie = movies.find_one({"_id": review["movieId"]})
    user = users.find_one({"_id": review["userId"]})

    print(f"""
Movie  : {movie['Title']}
User   : {user['username']}
Rating : {review['rating']}
""")