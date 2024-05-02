import pandas as pd
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

        self.nom_assureur = nom_assureur
        self.marge = marge

        if not isinstance(nom_assureur, str):
            raise TypeError("Le nom doit être une instance de str.")

        if not isinstance(marge, float):
            raise TypeError("La marge doit être un float.")

    def __donner_prix(self, data, localisation, categorie):
        """
        Détermine le prix qu'un client va payer

        Parameters
        ----------
        localisation : list[str]
            Liste des zones dans lesquelles le client se déplace.

        vehicule : str
            Véhicule du client qui souhaite être assuré.

        Returns
        -------
        prix : float
            Prix que va devoir payer le client chez cet assureur.

        """
        if not isinstance(localisation, list):
            raise TypeError("La localisation doit être une liste de rues")

        indicateur_risque = 0
        for k in len(localisation):
            indicateur_risque = (
                indicateur_risque + Utilisateur.risque_rue(data, localisation[k], categorie)
                )
        prix = (400 * indicateur_risque) * (1 + self.marge)
        return prix

    def __repr__(self, localisation: list[str], vehicule) -> str:
        """

        Représentation officielle de la réponse de l'assureur au client
        lui indiquant combien il doit payer.

        """
        return (f"Pour assurer votre véhicule de type, vous devez vous"
                f"acquitter de"
                f" {self.__donner_prix(localisation, vehicule)}")
