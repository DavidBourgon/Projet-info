# avant toute chose on a besoin de folium pour générer une carte :
# pip install folium
# on a également besoin de geopy et de geolocator pour transformer
# des adresses en coordonnées :
# pip install geopy
# pip install geolocator
# on a besoin de créer un itinéraire avec pyroutelib3 :
# pip install pyroutelib3
import folium
import webbrowser
# webbrowser sert à afficher la carte en language html.
from geopy.geocoders import Nominatim
from pyroutelib3 import Router
# router sert à préciser le type de vehicule qui peut être : car, cycle, foot,
#  horse, tram, train


class Particulier:
    """ Particulier.

    Décrit un particulier.

    Parameters
    ----------
    pieton : bool
        Indique si l'utilisateur concerné est un piéton ou non.

    velo : bool
        Indique si l'utilisateur concerné est un cycliste ou non.

    vehicule : bool
        Indique si l'utilisateur concerné est un conducteur ou non.

    """
    def __init__(pieton, velo, vehicule):
        pass

    def itineraires(self, adresse_depart, adresse_arrivee):
        # chargement et centrage de la carte
        carte_bronx = folium.Map(location=[40.8448, -73.8648], zoom_start=12)
        geolocator = Nominatim(user_agent="carte_bronx")
        # coordonnées des 2 adresses
        localisation_1 = geolocator.geocode(adresse_depart)
        coord_depart = (localisation_1.latitude, localisation_1.longitude)
        localisation_2 = geolocator.geocode(adresse_arrivee)
        coord_arrivee = (localisation_2.latitude, localisation_2.longitude)
        # ajout des points de depar et d'arrivee à la carte
        folium.Marker(coord_arrivee, popup='Départ').add_to(carte_bronx)
        folium.Marker(coord_depart, popup='Arrivée').add_to(carte_bronx)
        # creation de l'itineraire
        L = ["car", "cycle", "foot"]
        itineraires = {"car": [], "cycle": [], "foot": []}
        for vehicule in L:
            # ici on parle de noeud car la carte est un graphe
            noeud_depart = Router(vehicule).findNode(*coord_depart)
            noeud_arrivee = Router(vehicule).findNode(*coord_arrivee)
            status, route = Router(vehicule).doRoute(noeud_depart, noeud_arrivee)
            coordonnees_route = [Router(vehicule).nodeLatLon(node) for node in route]
            itineraires[vehicule] = coordonnees_route
        return itineraires

    def evaluate_risque_itineraire(self, adresse_depart, adresse_arrivee):
        # chargement et centrage de la carte
        carte_bronx = folium.Map(location=[40.8448, -73.8648], zoom_start=12)
        geolocator = Nominatim(user_agent="carte_bronx")
        # chargement des dictionnaires utiles
        itineraires = self.itineraires(adresse_depart, adresse_arrivee)
        risques = {"car": 1, "cycle": 1, "foot": 1}
        L = ["car", "cycle", "foot"]
        for vehicule in L:
            Iti_coord = itineraires[vehicule]
            # on va voir besoin du nombre total de points pour renvoyer
            # la moyenne du risque dans le dictionnaire
            tot_points = len(Iti_coord)
            compteur = 0
            for i in range(len(Iti_coord)):
                # Pour matcher avec les fonction morts risque_rue de Xavier,
                # on trouve le nom de la rue pour les coordonnées données
                localisation = geolocator.reverse(Iti_coord[i])
                address = localisation.raw['address']
                # Récupérer le nom de la rue si disponible
                nom_rue = address.get('road', None)
                # Là on peut utiliser les fonctions de Xavier,
                # il nous faudrait juste un fonction globale et
                # un filtrage par vehicule possible pour faire :
                compteur += jsp_quel_type.calculer_risque_rue(nom_rue, vehicule)
            risques[vehicule] = compteur/tot_points
        return risques

    def eviter_zone_risquee(self, adresse_depart, adresse_arrive):
        # Chargement de la carte
        carte_bronx = folium.Map(location=[40.8448, -73.8648], zoom_start=12)
        geolocator = Nominatim(user_agent="carte_bronx")
        dico_itineraires = self.itineraires(adresse_depart, adresse_arrivee)
        dico_risque = self.evaluate_risque_itineraire(adresse_depart, adresse_arrivee)
        vehicule_moins_risque = "car"
        risque = 2
        for vehicule in dico_risque:
            if dico_risque[vehicule] < risque:
                risque = dico_risque[vehicule]
                vehicule_moins_risque = vehicule
        if self.type_vehicule == vehicule_moins_risque:
            # on trace l'itineraire
            folium.PolyLine(locations=dico_itineraires[vehicule], color='blue').add_to(carte_bronx)
            webbrowser.open('carte_bronx.html')
            return ("Vous avez choisi le mode de transport le moins risqué,"
                    "voici votre itinéraire :")
        else:
            # on trace l'itineraire
            folium.PolyLine(locations=dico_itineraires[vehicule_moins_risque], color='blue').add_to(carte_bronx)
            webbrowser.open('carte_bronx.html')
            return ("Choisissez plutôt ce type de vehicule"
                    f"{vehicule_moins_risque}, voici l'itineraire")
