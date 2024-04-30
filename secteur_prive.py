import pandas as pd
from type_vehicule import TypeDeVehicule


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
    def __init__(self, nom_assureur: str, marge: float):

        self.nom_assureur = nom_assureur
        self.marge = marge

        if not isinstance(nom_assureur, str):
            raise TypeError("Le nom doit être une instance de str.")

        if not isinstance(marge, float):
            raise TypeError("La marge doit être un float.")

    def calculer_mortalite_rue(self, rue: str) -> float:
        pass

    def __calculer_risque_rue(self, vehicule, rue: str) -> float:

        if not isinstance(rue, str):
            raise TypeError("La rue doit être une instance de str.")

        if not isinstance(vehicule, TypeDeVehicule):
            raise TypeError("Le nom du vehicule n'est pas correct.")
        pass

    def __donner_prix(self, localisation: list[str], vehicule) -> float:
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
            raise TypeError("La localisation doit être une liste.")
            indicateur_risque = 0
            for k in len(localisation):
                indicateur_risque = (
                    indicateur_risque +
                    self.__calculer_risque_rue(vehicule, localisation[k])
                    )
            prix = (400 * indicateur_risque) * (1 + self.marge)
            return prix

    def __repr__(self, localisation: list[str], vehicule) -> str:
        return (f"Pour assurer votre véhicule de type, vous devez vous"
                f"acquitter de"
                f" {self.__donner_prix(localisation, vehicule)}")
