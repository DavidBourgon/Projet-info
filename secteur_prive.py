from Utilisateur import Utilisateur


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

    def __decompose_trajet(adresse_depart, adresse_arrrive):
        """
        Décompose un trajet entre 2 adresses.

        Prameters
        ---------
        adresse_depart : str
            Adresse de départ.

        adresse_arrivee : str
            Adresse d'arrivée.

        Retunrs
        -------
        localisation : list[str]
            liste des rues qu'il faut emprunter pour réaliser le trajet
            entre les 2 adresses données en entrée.
        """
        pass

    def __donner_prix(self, data, localisation, categorie):
        """
        Détermine le prix qu'un client va payer en fonction de comment
        il se déplace sur son trajet le plus fréquent

        Parameters
        ----------
        localisation : list[str]
            Liste des zones dans lesquelles le client se déplace.

        catégorie : str
            Véhicule du client qui souhaite être assuré.

        Returns
        -------
        prix : float
            Prix que va devoir payer le client chez cet assureur.

        """
        if not isinstance(localisation, list):
            raise TypeError("La localisation doit être une liste de rues")

        ind_risque = 0
        for k in len(localisation):
            ind_risque += Utilisateur.risque_rue(data,
                                                 localisation[k],
                                                 categorie)
        prix = (400 * ind_risque) * (1 + self.marge)
        return prix

    def __repr__(self, localisation: list[str], categorie):
        """

        Représentation officielle de la réponse de l'assureur au client
        lui indiquant combien il doit payer.

        """
        return (f"Pour vous assurer sur votre trajet quotidien,"
                f" vous devez vous acquitter de"
                f" {self.__donner_prix(localisation, categorie)}")
