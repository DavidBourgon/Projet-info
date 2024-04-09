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

    def __calculer_risque_rue(self, vehicule: Type_de_Vehicule,
                              rue: str) -> float:
        pass

    def __donner_prix(self, localisation: list[str], type_de_vehicule) -> float:
        pass

    def __repr__(self, localisation: list[str], type_de_vehicule) -> str:
        return (f"Pour assurer votre véhicule de type, vous devez vous"
                f"acquitter de"
                f" {self.__donner_prix(localisation, type_de_vehicule)}")
