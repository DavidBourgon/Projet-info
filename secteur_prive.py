import pandas as pd
from type_vehicule import TypeDeVehicule


class SecteurPrive:
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
        if not isinstance(localisation, list):
            raise TypeError("La localisation doit être une liste.")
            indicateur_risque = 0
            for k in len(localisation):
                indicateur_risque = (
                    indicateur_risque +
                    self.__calculer_risque_rue(vehicule, localisation[k])
                    )

    def __repr__(self, localisation: list[str], vehicule) -> str:
        return (f"Pour assurer votre véhicule de type, vous devez vous"
                f"acquitter de"
                f" {self.__donner_prix(localisation, vehicule)}")
