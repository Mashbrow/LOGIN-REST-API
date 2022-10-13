# LOGIN-REST-API
Repository for practical work on REST API 

### Installation
First clone the repo: `git clone https://github.com/Mashbrow/LOGIN-REST-API`

To launch with docker-compose, get to the LOGIN-REST-API folder and type `docker-compose up` in your terminal. Then use the requests of the REST servicies.  

### What was done so far

- Green Practical Work completely done.
- Blue version done with two different manners:
  - First version is in `movie`. Recommandations are sent in the response json directly.
  - Version 2 is in `movie2`. A GET `help`and a GET `reco` are added as access point to propose recommandations based on the last request accessed.
  Indeed, both present drawbacks (response modification or global variables insertions in the code) so we decided to propose both.
- Red version is completely done, it can be tested with the following access point `/movies/wikipedia/tt1375666` where `tt1375666` can be replaced by any other movie id in the imdb database.

## BOOKING
Folder containing the Booking service.  
Port:3201  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/booking": returns the booking database as a json.  
"/booking/&lt;userid&gt;": returns the bookings for a particular user as a json.  

Posts:  
"booking/&lt;userid&gt;": takes a booking as request, adds a booking for the user.  

## MOVIE
Folder containing the movie service.  
Port:3200  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/template": returns the homepage following a template.  
"/json":returns the movie database as a json.  
"/movie/&lt;movieid&gt;": returns the data for a particular movie as a json.  
"/moviebytitle": takes a movie title as request, returns the data for this particular movie as a json.  

Posts:  
"/movie/&lt;movieid&gt;": takes a movie as request, adds a movie to the database.  

Puts:   
"/movie/&lt;movieid&gt;/&lt;rate&gt;": changes the rating for a given movie.  

## MOVIE2
Folder containing the movie service.  
Port:3204  
Host: localhost  
Gets: Same as movie, but with the following gets added:  
"/help": gives you indications on how to use reco.  
"/reco": gives you a recommandation of what to do next.  

## SHOWTIME 
Folder containing the showtime service.  
Port:3202  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/showtime": returns the showtime database as a json.  
"/showtime/&lt;date&gt;": returns the shows for a particular date as a json.  

## USER
Folder containing the user service.  
Port:3203  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/user": returns the user database as a json.  
"/user/&lt;userid&gt;": returns the user's average rating.
