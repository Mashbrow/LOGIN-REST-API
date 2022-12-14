from flask import Flask, render_template, request, jsonify, make_response
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

#Init config 
PORT = 3202
HOST = '0.0.0.0'

#Load database
with open('{}/databases/times.json'.format("."), "r") as jsf:
   schedule = json.load(jsf)["schedule"]

#Index route
@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the Showtime service!</h1>"

#Get all schedules
@app.route("/showtime", methods=['GET'])
def get_schedule():
   res = make_response(jsonify(schedule), 200)
   return res

#Get the schedule for a specific date
@app.route("/showtime/<date>", methods=['GET'])
def get_movies_by_date(date):
   res = []
   for s in schedule:
      if s["date"] == date:
         res = make_response(jsonify(s),200)
         return res
   return make_response(jsonify({"bad input parameter"}), 400)


if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
