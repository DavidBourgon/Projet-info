import pandas as pd
import bordel_xavier as bx


data = pd.read_excel("BdD_Bronx.xlsx")


class SecteurPublic:
    """ Secteur Public

    Parameters
    ----------
    pieton : bool
        indique si l'utilisateur concerné est un piéton ou non

    velo : bool
        indique si l'utilisateur concerné est un cycliste ou non

    vehicule : bool
        indique si l'utilisateur concerné est un conducteur ou non
    """
    def __init__(self, pieton, velo, vehicule):
        self.pieton = pieton
        self.velo = velo
        self.vehicule = vehicule
        if not isinstance(vehicule, TypeDeVehicule):
            raise TypeError("Le véhicule doit être une instance de "
                            "TypeDeVehicule.")

    def calculer_mortalité_rue(rue: str):
        return bx.nmbr_mort_total(data)/bx.nmbr_mort_total_rue(data)

    def __localiser_infrastructure(zones: dict[int: list[str]]):
        pass
