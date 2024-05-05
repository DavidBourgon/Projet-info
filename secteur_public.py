import pandas as pd
import bordel_xavier as bx


data = pd.read_excel("BdD_Bronx.xlsx")


class SecteurPublic:
    """ Secteur Public.

    Décrit le secteur public.

    Parameters
    ----------
    categorie : str
        Catégorie du secteur public : institut de statistiques ou forces de
        l'ordre.

    """

    def __init__(self, categorie):
        self.categorie = categorie

        if not isinstance(categorie, str):
            raise TypeError("La catégorie doit être une chaîne de caractères.")

        if categorie not in ("institut_de_statistiques", "forces_de_l_ordre"):
            raise ValueError("La catégorie doit valoir "
                             "institut_de_statistiques ou "
                             "force_de_l_ordre.")

    def calculer_mortalité_rue(self, rue: str) -> int:
        """ Calcule le taux de mortalité d'une rue.

        Parameters
        ----------
        rue : str
            Nom de la rue dont on veut calculer le taux de mortalité.

        Returns
        -------
        str : Taux de mortalité de la rue demandée.

        """
        if not isinstance(rue, str):
            raise TypeError("La rue donnée doit être de type str.")

        taux_mortalité = bx.nmbr_mort_total_rue(data)/bx.nmbr_mort_total(data)
        return f"Le taux de mortalité de la rue {rue} est {taux_mortalité}."

    def __localiser_infrastructure(self, zones: dict[int: list[str]]):
        """ Permet de savoir où localiser des structures publiques parmi
        certaines zones sélectionées.

        Parameters
        ----------
        zones : dict[int: list[str]]
            Dictionnaire contenant les zones sélectionnées auxquelles des
            numéros sont attribués.

        Returns
        -------
        int : Numéro de la zone où localiser l'infrastructure.

        """
        pass
