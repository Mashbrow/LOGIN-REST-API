from flask import Flask, render_template, request, jsonify, make_response
import json
import requests
import sys
from werkzeug.exceptions import NotFound

app = Flask(__name__)

#Init Config
PORT = 3200
HOST = '0.0.0.0'

#Load Database
with open('{}/databases/movies.json'.format("."), "r") as jsf:
   movies = json.load(jsf)["movies"]

#Load probabilities from a dummy file, simulating the results of a ML Algorithm
#Probabilities will be used to orientate the discovery of the API
with open('{}/dummy_probs.json'.format("."), "r") as prb:
    probs = json.load(prb)

#Define function to give recommandation based on the probabilities
#The route with the maximum probabilities will be recommanded
def get_reco(access_point):
    vals = list(probs[access_point].values())
    keys = list(probs[access_point].keys())
    idx =  vals.index(max(vals))
    reco = keys[idx]
    return reco

# root message
@app.route("/", methods=['GET'])
def home():
    reco = get_reco("/")
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>" + "Most next accessed get request is: " + reco,200)

#Example of rendering a template
@app.route("/template", methods=['GET'])
def template():
    reco = get_reco("/template")
    return make_response(render_template('index.html', body_text='This is my HTML template for Movie service' + 'Most next accessed get request is: ' + reco),200)

#Get the whole movie db 
@app.route("/json", methods=['GET'])
def get_json():
    reco = get_reco("/json")
    
    res = make_response(jsonify({"movies":movies,"Most accessed get request": reco}), 200)
    return res

#Get movie by specifying an id in the path
@app.route("/movies/<movieid>", methods=['GET'])
def get_movie_byid(movieid):
    reco = get_reco("/movies/<movieid>")
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            res = make_response(jsonify({"movie": movie, "Most accessed get request":reco}),200)
            return res
    return make_response(jsonify({"error":"Movie ID not found"}),400)

#Get movie by specifying the title in the query
@app.route("/moviesbytitle", methods=['GET'])
def get_movie_bytitle():
    reco = get_reco("/moviesbytitle")
    json = ""
    if request.args:
        req = request.args
        for movie in movies:
            if str(movie["title"]) == str(req["title"]):
                json = movie

    if not json:
        res = make_response(jsonify({"error":"movie title not found"}),400)
    else:
        res = make_response(jsonify({"movie":json, "Most accessed get request":reco}),200)
    return res

#Add movie in the db specifying an ID
@app.route("/movies/<movieid>", methods=['POST'])
def create_movie(movieid):
    req = request.get_json()

    for movie in movies:
        if str(movie["id"]) == str(movieid):
            return make_response(jsonify({"error":"movie ID already exists"}),409)

    movies.append(req)
    res = make_response(jsonify({"message":"movie added"}),200)
    return res

#Modifying rating of a movie by specifying id and rate in the path
@app.route("/movies/<movieid>/<rate>", methods=['PUT'])
def update_movie_rating(movieid, rate):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movie["rating"] = int(rate)
            res = make_response(jsonify(movie),200)
            return res

    res = make_response(jsonify({"error":"movie ID not found"}),201)
    return res

#Delete movie by specifying an id in the path
@app.route("/movies/<movieid>", methods=['DELETE'])
def del_movie(movieid):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movies.remove(movie)
            return make_response(jsonify(movie),200)

    res = make_response(jsonify({"error":"movie ID not found"}),400)
    return res

#Request the IMDB database to get the wikipedia page plain text of a movie
# by specifying an ID
@app.route("/movies/wikipedia/<movieid>", methods=['GET'])
def get_imdb_wikipedia(movieid):
    imdb_response = requests.get("https://imdb-api.com/fr/API/Wikipedia/k_3huc73c2/" + movieid)
    json_imdb = imdb_response.json()
    return make_response(jsonify(json_imdb), 200)

if __name__ == "__main__":
    #p = sys.argv[1]
    print("Server running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)
