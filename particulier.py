import pandas as pd


class Particulier:
    """ Particulier.

    Décrit un particulier.

    Parameters
    ----------
    pieton : bool
        Indique si l'utilisateur concerné est un piéton ou non.

    velo : bool
        Indique si l'utilisateur concerné est un cycliste ou non.

    vehicule : bool
        Indique si l'utilisateur concerné est un conducteur ou non.

    """
    def __init__(pieton, velo, vehicule):
        pass

    def eviter_zone_risquee(self, heure_depart: time,
                            heure_arrive):
        pass
