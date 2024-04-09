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

    def calculer_mortalité_rue(self, rue: str) -> int:
        """ Calcule le taux de mortalité d'une rue.

        Parameters
        ----------
        rue : str
            Nom de la rue dont on veut calculer le taux de mortalité

        Returns
        -------
        str : taux de mortalité de la rue demandée

        """
        taux_mortalité = bx.nmbr_mort_total(data)/bx.nmbr_mort_total_rue(data)
        return f"Le taux de mortalité de la rue {rue} est {taux_mortalité}."

    def __localiser_infrastructure(self, zones: dict[int: list[str]]):
        pass
