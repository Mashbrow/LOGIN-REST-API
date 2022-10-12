# LOGIN-REST-API
Repository for practical work on REST API  
To launch with docker-compose, get to the LOGIN-REST-API folder and type `docker-compose up`` in your terminal. Then use the requests of the REST servicies.  

## BOOKING
Folder containing the Booking service.  
Port:3201  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/booking": returns the booking database as a json.  
"/booking/<userid>": returns the bookings for a particular user as a json.  

Posts:  
"booking/<userid>": takes a booking as request, adds a booking for the user.  

## MOVIE
Folder containing the Booking service.  
Port:3200  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/template": returns the homepage following a template.  
"/json":returns the movie database as a json.  
"/movie/<movieid>": returns the data for a particular movie as a json.  
"/moviebytitle": takes a movie title as request, returns the data for this particular movie as a json.  

Posts:  
"/movie/<movieid>": takes a movie as request, adds a movie to the database.  

Puts:   
"/movie/<movieid>/<rate>": changes the rating for a given movie.  

## SHOWTIME 
Folder containing the Booking service.  
Port:3202  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/showtime": returns the showtime database as a json.  
"/showtime/<date>": returns the shows for a particular date as a json.  

## USER
Folder containing the Booking service.  
Port:3203  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/user": returns the user database as a json.  
"/user/<userid>": returns the user with this id as a json.  
