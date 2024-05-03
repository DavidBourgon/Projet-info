# # avant toute chose on a besoin de folium pour générer une carte :
# pip install folium
# # on a également besoin de geopy et de geolocator pour transformer
# # des adresses en coordonnées :
# pip install geopy
# pip install geolocator
# # on a besoin de créer un itinéraire avec pyroutelib3 :
# pip install pyroutelib3
import folium
import webbrowser  # webbrowser sert à afficher la carte en language html.
from geopy.geocoders import Nominatim
from pyroutelib3 import Router
from Utilisateur import Utilisateur
import pandas as pd
# router sert à préciser le type de vehicule qui peut être : car, cycle, foot,
# horse, tram, train


class Particulier:
    """ Particulier.

    Décrit un particulier.

    Parameters
    ----------
    categorie : str
        Catégorie de l'usagé : piéton, cycliste ou automobiliste. Elle vaut
        soit foot pour les piétons, soit cycle pour les cyclistes soit car
        pour les automobilistes.

    """
    def __init__(self, categorie):
        self.categorie = categorie

        if not isinstance(categorie, str):
            raise TypeError("La catégorie doit être une chaîne de caractères.")

        if categorie not in ("foot", "cycle", "car"):
            raise ValueError("La catégorie doit valoir foot, cycle ou "
                             "car.")

    def itineraires(self, adresse_depart, adresse_arrivee):
        """
        Permet de déterminer un itinéraire entre 2 adresses du Bronx.

        Parameters
        ----------
        adresse_depart : str
            Adresse de départ.

        adresse_arrivee : str
            Adresse d'arrivée.

        Retunrs
        -------
        itineraires : dict[str : list]
            Dictionnaire d'itinéraires selon le type de véhicule.
            str : Moyen de transport utilisé.
            list : Itinéraire.

        """
        # if not isinstance(adresse_depart, str):
        #     raise TypeError("L'adresse de départ doit être un str.")
        # elif not adresse_depart.endswith(', New York'):
        #     raise ValueError("La chaîne de caractères doit se "
        #                      "terminer par ', New York'.")
        # elif not adresse_depart.split(',')[0].strip().isalpha():
        #     raise TypeError("Le début de la chaîne de caractères "
        #                     "doit être str.")

        # if not isinstance(adresse_arrivee, str):
        #     raise TypeError("L'adresse de départ doit être un str.")
        # elif not adresse_arrivee.endswith(', New York'):
        #     raise ValueError("La chaîne de caractères doit se "
        #                      "terminer par ', New York'.")
        # elif not adresse_arrivee.split(',')[0].strip().isalpha():
        #     raise TypeError("Le début de la chaîne de caractères "
        #                     "doit être str.")

        # chargement et centrage de la carte
        carte_bronx = folium.Map(location=[40.8448, -73.8648], zoom_start=12)
        geolocator = Nominatim(user_agent="carte_bronx")
        # coordonnées des 2 adresses
        localisation_1 = geolocator.geocode(adresse_depart)
        coord_depart = (localisation_1.latitude, localisation_1.longitude)
        localisation_2 = geolocator.geocode(adresse_arrivee)
        coord_arrivee = (localisation_2.latitude, localisation_2.longitude)
        # creation de l'itineraire
        L = ["car", "cycle", "foot"]
        itineraires = {"car": [], "cycle": [], "foot": []}
        for vehicule in L:
            router = Router(vehicule)
            # ici on parle de noeud car la carte est un graphe
            node_depart = router.findNode(*coord_depart)
            node_arrivee = router.findNode(*coord_arrivee)
            status, route = router.doRoute(node_depart, node_arrivee)
            coordonnees_route = [router.nodeLatLon(node) for node in route]
            itineraires[vehicule] = coordonnees_route
        return itineraires

    def evaluate_risque_itineraire(self, adresse_depart, adresse_arrivee):
        """
        Permet de déterminer le risque des itinéraires entre 2 adresses du
        Bronx.

        Parameters
        ----------
        adresse_depart : str
            Adresse de départ.

        adresse_arrivee : str
            Adresse d'arrivée.

        Returns
        -------
        itineraires : dict[str : float]
            Dictionnaire de risque d'itinéraires selon le type de véhicule.
            str : Moyen de transport utilisé.
            float : Risque de l'itinéraire.

        """
        # chargement et centrage de la carte
        carte_bronx = folium.Map(location=[40.8448, -73.8648], zoom_start=30)
        geolocator = Nominatim(user_agent="carte_bronx")
        data = pd.read_excel("Bronx_2.xlsx")
        # chargement des dictionnaires utiles
        itineraires = self.itineraires(adresse_depart, adresse_arrivee)
        risques = {"car": 1.0, "cycle": 1.0, "foot": 1.0}
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
                # On met le nom de la rue en majuscules pour correspondre à
                # la base de données.
                nom_rue_maj = nom_rue.upper()
                print(nom_rue_maj)
                # Là on peut utiliser les fonctions de Xavier,
                # il nous faudrait juste un fonction globale et
                # un filtrage par vehicule possible pour faire :
                compteur += Utilisateur.risque_rue(data, nom_rue_maj, vehicule)[-1]
            risques[vehicule] = compteur/tot_points
        return risques

    def eviter_zone_risquee(self, adresse_depart, adresse_arrivee):
        """
        Permet de déterminer le moyen de transport pour lequel l'itinéraire est
        le moins risqué entre 2 adresses du Bronx.

        Parameters
        ----------
        adresse_depart : str
            Adresse de départ.

        adresse_arrivee : str
            Adresse d'arrivée.

        Retunrs
        -------
        str : Phrase indiquant le moyen de transport à choisir pour avoir le
              moins de risques.
        map : Carte du meilleur itinéraire en vert et des 2 autres itinéraires
              plus risqués en rouge.

        """
        # Chargement de la carte
        carte_bronx = folium.Map(location=[40.8448, -73.8648], zoom_start=12)
        geolocator = Nominatim(user_agent="carte_bronx")
        dico_itineraires = self.itineraires(adresse_depart, adresse_arrivee)
        dico_risque = self.evaluate_risque_itineraire(adresse_depart,
                                                      adresse_arrivee)
        vehicule_moins_risque = "car"
        risque = 2
        localisation_1 = geolocator.geocode(adresse_depart)
        coord_depart = (localisation_1.latitude, localisation_1.longitude)
        localisation_2 = geolocator.geocode(adresse_arrivee)
        coord_arrivee = (localisation_2.latitude, localisation_2.longitude)
        folium.Marker(coord_depart, popup='Adresse de départ').add_to(carte_bronx)
        folium.Marker(coord_arrivee, popup='Adresse d\'arrivée').add_to(carte_bronx)
        for vehicule in dico_risque:
            if dico_risque[vehicule] < risque:
                risque = dico_risque[vehicule]
                vehicule_moins_risque = vehicule
        if self.categorie == vehicule_moins_risque:
            # on trace l'itineraire
            for vehicule in ["car", "cycle", "foot"]:
                if vehicule != vehicule_moins_risque:
                    folium.PolyLine(locations=dico_itineraires[vehicule],
                            color='red').add_to(carte_bronx)
            folium.PolyLine(locations=dico_itineraires[vehicule],
                            color='green').add_to(carte_bronx)
            carte_bronx.save("carte_bronx.html")
            webbrowser.open('carte_bronx.html')
            return ("Vous avez choisi le mode de transport le moins risqué,"
                    "voici votre itinéraire :")
        else:
            # on trace l'itineraire
            for vehicule in ["car", "cycle", "foot"]:
                if vehicule != vehicule_moins_risque:
                    folium.PolyLine(locations=dico_itineraires[vehicule],
                            color='red').add_to(carte_bronx)
            folium.PolyLine(locations=dico_itineraires[vehicule_moins_risque],
                            color='green').add_to(carte_bronx)
            carte_bronx.save("carte_bronx.html")
            webbrowser.open('carte_bronx.html')
            return ("Choisissez plutôt ce type de vehicule : "
                    f"{vehicule_moins_risque}, voici l'itineraire")


#Xavier = Particulier("foot")
#print(Xavier.eviter_zone_risquee("1 E 161st St, Bronx, NY 10451, États-Unis", "111 E 164th St, Bronx, NY 10452, États-Unis"))
