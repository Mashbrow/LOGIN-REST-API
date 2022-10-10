from flask import Flask, render_template, request, jsonify, make_response
import json
import requests
import sys
from werkzeug.exceptions import NotFound

app = Flask(__name__)

PORT = 3204
HOST = '0.0.0.0'

with open('{}/databases/movies.json'.format("."), "r") as jsf:
    movies = json.load(jsf)["movies"]

last_used = "None"

dic_reco={
    "None":"/",
    "/help" :"/reco",
    "/reco" : "/",
    "/": "/json",
    "/template":"/json",
    "/json": "/movies/<movieid>",
    "/movies/<movieid>": "/moviesbytitle",
    "/moviesbytitle": "/movies/<movieid>",
}

@app.route("/help", methods=['GET'])
def get_help():
    return make_response("If you wonder what to do next, use the reco method.",200)

@app.route("/reco", methods=['GET'])
def get_reco():
    global last_used
    if last_used == "None":
        return make_response("The first method to be used is usually "+dic_reco[str(last_used)])
    return make_response("After using "+last_used+", most people use " + dic_reco[str(last_used)] + " next.",200)



# root message
@app.route("/", methods=['GET'])
def home():
    global last_used
    last_used = "/"
    return make_response(
        "<h1 style='color:blue'>Welcome to the Movie service!</h1>",200)


@app.route("/template", methods=['GET'])
def template():
    global last_used
    last_used = "/template"
    return make_response(render_template('index.html',
                                         body_text='This is my HTML template for Movie service'),
                         200)


@app.route("/json", methods=['GET'])
def get_json():
    global last_used
    last_used = "/json"
    res = make_response(jsonify({"movies": movies}), 200)
    return res


@app.route("/movies/<movieid>", methods=['GET'])
def get_movie_byid(movieid):
    global last_used
    last_used = "/movies/<movieid>"
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            res = make_response(jsonify({"movie": movie}), 200)
            return res
    return make_response(jsonify({"error": "Movie ID not found"}), 400)


@app.route("/moviesbytitle", methods=['GET'])
def get_movie_bytitle():
    global last_used
    last_used = "/moviesbytitle"
    json = ""
    if request.args:
        req = request.args
        for movie in movies:
            if str(movie["title"]) == str(req["title"]):
                json = movie

    if not json:
        res = make_response(jsonify({"error": "movie title not found"}), 400)
    else:
        res = make_response(jsonify({"movie": json, "Most accessed get request": reco}), 200)
    return res


@app.route("/movies/<movieid>", methods=['POST'])
def create_movie(movieid):
    req = request.get_json()

    for movie in movies:
        if str(movie["id"]) == str(movieid):
            return make_response(jsonify({"error": "movie ID already exists"}), 409)

    movies.append(req)
    res = make_response(jsonify({"message": "movie added"}), 200)
    return res


@app.route("/movies/<movieid>/<rate>", methods=['PUT'])
def update_movie_rating(movieid, rate):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movie["rating"] = int(rate)
            res = make_response(jsonify(movie), 200)
            return res

    res = make_response(jsonify({"error": "movie ID not found"}), 201)
    return res


@app.route("/movies/<movieid>", methods=['DELETE'])
def del_movie(movieid):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movies.remove(movie)
            return make_response(jsonify(movie), 200)

    res = make_response(jsonify({"error": "movie ID not found"}), 400)
    return res


@app.route("/movies/wikipedia/<movieid>", methods=['GET'])
def get_imdb_wikipedia(movieid):
    imdb_response = requests.get("https://imdb-api.com/fr/API/Wikipedia/k_3huc73c2/" + movieid)
    json_imdb = imdb_response.json()
    return make_response(jsonify(json_imdb), 200)


if __name__ == "__main__":
    # p = sys.argv[1]
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT)
