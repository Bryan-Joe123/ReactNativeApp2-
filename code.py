from flask import Flask, jsonify, request 
from storage import all_movies, liked_movies, not_liked_movies, did_not_watch 
from demographic_filtering import output
from content_filtering import get_recommendations

# Creating the app
app=Flask(__name__)

# Functions to get the movies api
@app.route("/get-movie") 
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"Sucess"
    })

# Api to post liked movies
@app.route("/liked-movie",Methods=["POST"]) 
def liked_movie():
    movie=all_movies[0]
    temp_all_movies = all_movies[1:]
    # all_movies=temp_all_movies
    liked_movie.append(movie)

    return jsonify({
        "status":"Sucess"
    },201)

# Api to post disliked movies
@app.route("/disliked-movie",Methods=["POST"]) 
def disliked_movie():
    movie=all_movies[0]
    temp_all_movies = all_movies[1:]
    # all_movies=temp_all_movies
    disliked_movie.append(movie)

    return jsonify({
        "status":"Sucess"
    },201)

# Api to post never-watched-movies movies
@app.route("/never-watched-movies",Methods=["POST"]) 
def never_watched_movies():
    movie=all_movies[0]
    temp_all_movies = all_movies[1:]
    never_watched_movies.append(movie)

    return jsonify({
        "status":"Sucess"
    },201)
    
# Api to post never-watched-movies movies
@app.route("/popular-movies") 
def popular_movies():
    movie_data=[]
    for movie in output:
        _d = {
            "title":movie[0],
            "poster_link":movie[1],
            "release_data":movie[2] or "N/A",
            "duration":movie[3],
            "rating":movie[4],
            "over_view":movie[5]
        }
        
        movie_data.append(_d)

    return jsonify({
        "data":movie_data,
        "status":"Sucess"
    },200)

@app.route("/recommended-movies")
def recommended_movie():
    all_recommended = []
    for liked_movie in liked_movies:
        output=get_recommendations(liked_movie[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended=list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    
    movie_data = []
    for recommended in all_recommended:
        _d = {
            "title":recommended[0],
            "poster_link":recommended[1],
            "release_data":recommended[2] or "N/A",
            "duration":recommended[3],
            "rating":recommended[4],
            "over_view":recommended[5]
        }
        
        movie_data.append(_d)
        
    return jsonify({
        "data":movie_data,
        "status":"Sucess"
    },200)

#Run the whole app
if __name__ == "__main__":
    app.run()