from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound
from operator import itemgetter

app = Flask(__name__)

#Init Config
PORT = 3201 
HOST = '0.0.0.0'

#Loading db
with open('{}/databases/bookings.json'.format("."), "r") as jsf:
   bookings = json.load(jsf)["bookings"]

#Index route
@app.route("/", methods=['GET'])
def home():
   print("coucou" + request.host)
   return "<h1 style='color:blue'>Welcome to the Booking service!</h1>"

#Get all bookings
@app.route("/booking", methods=['GET'])
def get_json():
   res = make_response(jsonify(bookings), 200)
   return res

#Get bookings for a user specifying an ID in the path
@app.route("/booking/<userid>", methods=['GET'])
def get_booking_for_user(userid):
   for b in bookings:
      if b["userid"] == userid:
          return make_response(jsonify(b), 200)
   return make_response(jsonify({"error":"bad input parameter"}), 400)

#Add booking for a user by specifying an ID in the path
@app.route("/booking/<userid>", methods=['POST'])
def add_booking_by_user(userid):
   req = request.get_json()
   #### Verify that the movie is scheduled
   ## Request the showtime API
   host_ = 'http://' + request.host.split(':')[0]
   request_showtime = requests.get(host_ + ':' + '3202'+'/showtime')
   sch_dates = [sch["date"] for sch in request_showtime.json()]
   if req["date"] not in sch_dates:
      return make_response(jsonify({"error":"wrong date"}))
   sch_idx = sch_dates.index(req["date"])
   if req["movieid"] not in request_showtime.json()[sch_idx]["movies"]:
      return make_response(jsonify({"error": "movie not scheduled at this date"}))
   
   ### Verify that the booking doesn't exist and create it if so
   for b in bookings:
      if b["userid"] == userid:
         dates = [b_["date"] for b_ in b["dates"]]
         if req["date"] in dates:
            idx = dates.index(req["date"])
            if req["movieid"] in b["dates"][idx]["movies"]:
               return make_response(jsonify({"error":"an existing item already exists"}), 409)
            b["dates"][idx]["movies"].append(req["movieid"])
            return make_response(jsonify(b), 200)
         to_push = {"date" : req["date"], "movies" : [req["movieid"]]}
         b["dates"].append(to_push)
         return make_response(jsonify(b),200)
            
 
if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
