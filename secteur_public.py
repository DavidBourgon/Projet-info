import pandas as pd


class SecteurPublic:
    def __init__(self, pieton, velo, vehicule):
        self.pieton = pieton
        self.velo = velo
        self.vehicule = vehicule
        if not isinstance(vehicule, TypeDeVehicule):
            raise TypeError("Le véhicule doit être une instance de "
            "TypeDeVehicule.")

    def calculer_mortalité_rue(rue: str):
        pass

    def __localiser_infrastructure(zones: dict[int: list[str]]):
        pass
