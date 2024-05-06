from Utilisateur import Utilisateur
from geopy.geocoders import Nominatim
from pyroutelib3 import Router
import folium


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

    def __donner_prix(self, data, adresse_depart, adresse_arrivee, categorie):
        """
        Détermine le prix qu'un client va payer en fonction de comment
        il se déplace sur son trajet le plus fréquent

        Parameters
        ----------
        data : DataFrame
            Base de données sur laquelle nous travaillons.

        rues : list(str)
            Liste des rues dans lesquelles le client se déplace.

        catégorie : str
            Catégorie d'usagé à laquelle le client appartient. Prend la
            valeur foot cycle ou car.

        Returns
        -------
        prix : float
            Prix que va devoir payer le client chez cet assureur.

        """
        rues = self.__decompose_trajet(adresse_depart, adresse_arrivee,
                                       categorie)

        ind_risque = 0
        for k in len(rues):
            ind_risque += Utilisateur.risque_rue(data,
                                                 rues[k],
                                                 categorie)
        prix = (400 * (ind_risque/len(rues))) * (1 + self.marge)
        return prix

    def __repr__(self, data, adresse_depart, adresse_arrivee, categorie):
        """

        Représentation officielle de la réponse de l'assureur au client
        lui indiquant combien il doit payer.

        """
        prix = self.__donner_prix(data, adresse_depart,
                                  adresse_arrivee, categorie)
        return (f"Pour vous assurer sur votre trajet quotidien, auprès de "
                f"{self.nom_assureur} "
                f"vous devez vous acquitter de "
                f"{prix} €")
