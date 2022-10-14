## TP UE Services
Les rendus des tp sont divisés en 3 dossier, pour REST, GRPC et GRAPHQL.  
Le but de ces TP était de créer un service de gestion de réservations en faisant appel à 3 services (movie, booking et showtime) ainsi qu'à un client (user).   
![alt text](https://github.com/Mashbrow/LOGIN-REST-API/blob/main/graphe.png)
- Rest
  - TP vert effectué. Nous avons décidé de rajouter un point d'accès afin d'obtenir la moyenne des notes des films réservé. Nous trouvions pertinent de comparer la         note moyenne des films réservé par rapport aux notes données par le public. 
  - TP bleu effectué de deux versions différentes:
    - Version 1 dans `movie`. Des recommandations sont renvoyées dans la réponse aux GET.
    - Versions 2 dans movie2. Un GET `help` et un GET `reco` sont ajoutés pour proposer des recommandations en fonction du dernier GET.  
    En effet, les deux méthodes présentent des incovénients (modification des réponses ou insersion de variabels globales), et nous avons décidé de proposer les deux.
    L'objectif de ce TP bleu a été pour nous de simuler l'apport d'un module de machine learning qui prévoirait la prochaine requête d'un utilisateur en se basant sur     ses requêtes antérieures. Pour cela nous avons créer le fichier `dummy_probs.json` dans le dossier movie. Ce fichier contient des probabilités d'acceder à d'autres     points d'accès ce que l'on pourrait typiquement obtenir en sortie d'un modèle de machine learning.
    
  - TP rouge effectué, celui-ci peut être testé avec la méthode `localhost:3200/movies/wikipedia/tt1375666`, où `tt1375666`peut être remplacer par l'id de n'importe quel film présent dans la base de donnée IMDB. Concernant cette version du TP nous avons décidé de créer un point d'accès renvoyant la page wikipedia (uniquement le texte des paragraphes) du film correspondant à l'id. Ce point d'accès est utile pour obtenir de plus amples informations concernant le film.
  
- GRPC
  - TP vert effectué.
    - Les dossiers `user` et `booking` correspondent à la version du tp vert.
  - TP bleu effectué:
    - La version du TP bleu de booking est dans le dossier `booking-grpc`. Les dossiers `user2` et `booking_grpc` correspondent à la version du tp bleu.
  - TP rouge effectué:
    - La version du TP rouge de booking est dans le dossier `client` sous le nom `client_booking_asynchronous`. Il est à noté que la partie asynchrone n'est géré que du côté client, en effet, rien n'est à modifié du côté serveur. C'est pourquoi dans le TP rouge seul le client change et pas le service.
- GRAPHQL
  - TP vert effectué
    - Le dossier `movie` contient la version du TP vert GRAPHQL. Le reste des dossiers contiennent des versions GRPC ou REST.


## Concernant les Performances de ces trois API:

Nous avons décidé d'étudier les performances des 3 API en se basant sur le service movie précédemment mis en place sur les trois tps précédents.
