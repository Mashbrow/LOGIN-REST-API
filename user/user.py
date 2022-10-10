from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

#Init config
PORT = 3203
HOST = '0.0.0.0'

#Load database
with open('{}/databases/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

#Index route
@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"

#Get all Users
@app.route("/user", methods=['GET'])
def get_json():
   return make_response(jsonify(users), 200)

#Get the average rating over all the movies that were booked by a user
@app.route("/user/<userid>", methods=['GET'])
def get_average_user_rating(userid):
   #Find user
   r_sum = 0
   cond = False
   for element in users:
      if userid == element["id"]:
         cond = True
   if not cond:
      return make_response(jsonify({"error":"no user found"}), 400)
   
   #Request booking API to get all the booking of a user
   host_ = 'http://' + request.host.split(':')[0]
   request_booking = requests.get(host_ + ':' + '3201'+'/booking/'+str(userid))
   if request_booking.ok : 
      bookings = request_booking.json()
   else:
      return make_response({"error":"no movies booked for that user"}, 409)

   #Request movie API to get all the movies in the database 
   request_movie = requests.get(host_ + ':' + '3200' + '/json')
   movies_list = request_movie.json()['movies']

   #Get movie booked
   booked_movies = []
   for date in bookings["dates"]:
      booked_movies += date["movies"]

   #Get average rating over booked movies
   for b_movie in booked_movies:
      for m in movies_list:
         if b_movie == m["id"]:
            r_sum += m["rating"]

   average = r_sum/len(booked_movies)      
   return make_response(jsonify({"average_rating":average}), 200)

if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
