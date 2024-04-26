# avant toute chose on a besoin de folium pour générer une carte :
# pip install folium
# on a également besoin de geopy et de geolocator pour transformer des adresses en coordonnées :
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

    def eviter_zone_risquee(self, heure_depart: time,
                            heure_arrive):
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
        itineraires = self.itineraires(adresse_depart, adresse_arrivee)
        risques = {"car": 1, "cycle": 1, "foot": 1}
        L = ["car", "cycle", "foot"]
        for vehicule in L:
            Iti_coord = itineraires[vehicule]
            # on va voir besoin du nombre total de points pour renvoyer
            # la moyenne du risque dans le dictionnaire
            total_points = len(Iti_coord)
            for i in range(len(Iti_coord)):





        # on trace l'itineraire
        folium.PolyLine(locations=coordonnees_route, color='blue').add_to(carte_bronx)
        webbrowser.open('carte_bronx.html')