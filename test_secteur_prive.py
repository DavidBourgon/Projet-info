# from secteur_prive import SecteurPrive
# import pytest
# import pandas as pd
# import re


# @pytest.mark.parametrize(
#     'kwargs, erreur, message_erreur',
#     [
#         ({'nom_assureur': 12, 'marge': 0.25}, TypeError,
#          "Le nom doit être une instance de str."),
#         ({'nomm_assureur': ['Dupont'], 'marge': 0.3}, TypeError,
#          "Le nom doit être une instance de str."),
#         ({'nom_assureur': "Dupont", 'marge': "0.5"}, TypeError,
#          "La marge doit être un float."),
#         ({'nom_assureur': "Dupont", 'marge': [0.2]}, TypeError,
#          "La marge doit être un float."),
#         ({'nom_assureur': "Dupont", 'marge': 2}, TypeError,
#          "La marge doit être comprise entre 0 et 1."),
#         ({'nom_assureur': "Dupont", 'marge': -2}, TypeError,
#          "La marge doit être comprise entre 0 et 1."),

#     ]
# )
# def test_secteur_prive_init_echec(pompe_e85_kwargs,  kwargs, erreur,
#                                   message_erreur):
#     pompe_e85_kwargs.update(kwargs)
#     with pytest.raises(erreur, match=re.escape(message_erreur)):
#         SecteurPrive(**pompe_e85_kwargs)
