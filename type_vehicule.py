class TypeDeVehicule:
    """ Décrit le véhicule.
    Parameters
    ----------
    categorie: str
        Catégorie du véhicule.
    """
    def __init__(self, categorie: str) -> None:
        """ fonction
        """
        if not isinstance(categorie, str):
            raise TypeError("Le nom doit être une instance de str.")

