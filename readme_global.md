## TP UE Services
Les rendus des tp sont divisés en 3 dossier, pour REST, GRPC et GRAPHQL.  
Le but de ces TP était de créer un service de gestion de réservations en faisant appel à 3 services (movie, booking et showtime) ainsi qu'à un client (user).   
![alt text](https://github.com/Mashbrow/LOGIN-REST-API/blob/main/graphe.png)
- Rest
  - TP vert effectué.
  - TP bleu effectué de deux versions différentes:
    - Version 1 dans movie. Des recommandations sont renvoyées dans la réponse aux GET.
    - Versions 2 dans movie2. Un GET `help` et un GET `reco` sont ajoutés pour proposer des recommandations en fonction du dernier GET.  
    En effet, les deux méthodes présentent des incovénients (modification des réponses ou insersion de variabels globales), et nous avons décidé de proposer les deux.
  - TP rouge effectué, peut être testé avec la méthode `localhost:3200/movies/wikipedia/tt1375666`.
- GRPC
  - TP vert effectué.
    - Les dossiers user et booking correspondent à la version du tp vert.
  - TP bleu effectué:
    - La version du TP bleu de booking est dans le dossier `booking-grpc`. Les dossiers user2 et booking_grpc correspondent à la version du tp bleu.
  - TP rouge effectué:
    - La version du TP rouge de booking est dans le dossier `client` sous le nom `client_booking_asynchronous`.
- GRAPHQL
  - TP vert effectué
    - Le dossier movie contient la version du TP vert GRAPHQL. Le reste des dossiers contiennent des versions GRPC ou REST. 
