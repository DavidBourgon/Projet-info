from Utilisateur import Utilisateur
from geopy.geocoders import Nominatim
from pyroutelib3 import Router
import folium
import pandas as pd


class SecteurPrive:
    """ Secteur Privé.

    Décrit le secteur privé.

    Parameters
    ----------
    nom_assureur : str
        Nom de l'assureur du secteur.

    marge : float
        Marge que prend l'assureur.

    """
    def __init__(self, nom_assureur, marge):

        if not isinstance(nom_assureur, str):
            raise TypeError("Le nom doit être une instance de str.")

        if not isinstance(marge, float):
            raise TypeError("La marge doit être un float.")

        if not 0 <= marge <= 1:
            raise ValueError("La marge doit être comprise entre 0 et 1.")

        self.nom_assureur = nom_assureur
        self.marge = marge

    def __decompose_trajet(self, adresse_depart, adresse_arrivee, categorie):
        """
        Décompose un trajet entre 2 adresses.

        Prameters
        ---------
        adresse_depart : str
            Adresse de départ.

        adresse_arrivee : str
            Adresse d'arrivée.

        categorie : str
            Catégorie d'usagé à laquelle le client appartient. Prend la
            valeur foot cycle ou car.

        Retunrs
        -------
        localisation : list[str]
            liste des rues qu'il faut emprunter pour réaliser le trajet
            entre les 2 adresses données en entrée.

        """
        carte_bronx = folium.Map(location=[40.8448, -73.8648], zoom_start=12)

        # Coordonnées des 2 adresses
        geolocator = Nominatim(user_agent="carte_bronx")
        localisation_1 = geolocator.geocode(adresse_depart)
        coord_depart = (localisation_1.latitude, localisation_1.longitude)
        localisation_2 = geolocator.geocode(adresse_arrivee)
        coord_arrivee = (localisation_2.latitude, localisation_2.longitude)

        # Création de l'itinéraire
        router = Router(categorie)
        node_depart = router.findNode(*coord_depart)
        node_arrivee = router.findNode(*coord_arrivee)
        status, route = router.doRoute(node_depart, node_arrivee)

        # Récupération des noms des rues
        rues = set()
        for node in route:
            coordonnees = router.nodeLatLon(node)
            localisation = geolocator.reverse(coordonnees)
            adresse = localisation.raw['address']
            nom_rue = adresse.get('road', None)
            if nom_rue:
                rues.add(nom_rue)
        return list(rues)

    def risque_rue_naif(data, street, categorie):
        """
        Permet de calculer le danger d'une rue en %.

        Parameters
        ----------
        data : Dataframe
            Base de données sur laquelle nous travaillons.

        street : str
            Nom de la rue pour laquelle nous souhaitons déterminer le danger.

        categorie : str
            Catégorie d'usagés : piéton, cycliste ou automobiliste.

        Returns
        -------
        str : Phrase indiquant le danger en % pour la rue et la catégorie
              souhaitées.

        """
        data_street = Utilisateur.filtrer_par_nom_de_rue(data, street)[-1]
        n_tot = Utilisateur.nombre_observation(data)[-1]
        if n_tot == 0:
            return ["Il n'y a pas d'accident ou bien le tableau est vide.",
                    "Pour la rue :", street,
                    "Il y a un rique (en %) de :", 0]
        else:
            n_mort_cat = Utilisateur.\
                calcul_totaux_cat_statut(data_street, categorie, "T")[-1]
            n_blesse_cat = Utilisateur.\
                calcul_totaux_cat_statut(data_street, categorie, "B")[-1]

            n_mort_total = Utilisateur.\
                calcul_totaux_statut(data_street, "T")[-1]
            n_blesse_total = Utilisateur.\
                calcul_totaux_statut(data_street, "B")[-1]

            if n_mort_total == 0 and n_blesse_total == 0:
                risque = 0

            elif n_mort_total == 0:
                risque = 100*n_blesse_cat/n_blesse_total

            elif n_blesse_total == 0:
                risque = 100*n_mort_cat/n_mort_total

            else:
                risque = 100*(n_mort_cat/n_mort_total +
                              n_blesse_cat/n_blesse_total)/2

        return ["Pour la rue :", street,
                "il y a un rique (en %) de :", risque]

    def __donner_prix(self, data, adresse_depart, adresse_arrivee,
                      categorie, type_vehicule=None):
        """
        Détermine le prix qu'un client va payer en fonction de comment
        il se déplace sur son trajet le plus fréquent

        Parameters
        ----------
        data : DataFrame
            Base de données sur laquelle nous travaillons.

        adresse_depart : str
            Adresse de départ.

        adresse_arrivee : str
            Adresse d'arrivée.

        catégorie : str
            Catégorie d'usagé à laquelle le client appartient. Prend la
            valeur foot cycle ou car.

        type_vehicule : str
            Type de véhicule que le client possède.
            Vaut None par défaut.

        Returns
        -------
        prix : float
            Prix que va devoir payer le client chez cet assureur.

        """
        if type_vehicule is not None:
            data_par_type = Utilisateur.\
                filtrer_par_modalite_variable(data, type_vehicule,
                                              "VEHICLE.TYPE.CODE.1")[-1]
        else:
            data_par_type = data

        rues = self.__decompose_trajet(adresse_depart, adresse_arrivee,
                                       categorie)

        ind_risque = 0
        for k in range(len(rues)):
            street = rues[k].upper()
            ind_risque += SecteurPrive.risque_rue_naif(data_par_type,
                                                       street,
                                                       categorie)[-1]
        ind_normalise = (ind_risque/100)/len(rues)
        prix = (400 * ind_normalise) * (1 + self.marge) + 200
        return round(prix, 2)

    def __repr__(self, data, adresse_depart, adresse_arrivee,
                 categorie, type_vehicule=None):
        """

        Représentation officielle de la réponse de l'assureur au client
        lui indiquant combien il doit payer.

        """
        return (f"Pour vous assurer sur votre trajet quotidien, auprès de "
                f"{self.nom_assureur} "
                f"vous devez vous acquitter de "
                f"{self.__donner_prix(data, adresse_depart,
                                      adresse_arrivee, categorie,
                                      type_vehicule)} €")

# data = pd.read_excel("Bronx_sans_Na.xlsx")
# Groupama = SecteurPrive("Groupama", 0.8)
# print(Groupama.__repr__(data, "Heath Avenue, Bronx, New York",
#                         "Heath Avenue, Bronx, New York",
#                         "car", "Pick-up Truck"))
