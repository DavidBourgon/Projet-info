from Utilisateur import Utilisateur
import pytest
import pandas as pd
import re

data = pd.read_excel("Bronx_2.xlsx")


# Définition des cas de test pour nombre_observation échec
@pytest.mark.parametrize(
    'kwargs, erreur, message_erreur',
    [
        (2, TypeError,
         "La base de données doit être un DataFrame.")
    ]
)
def test_nombre_observation_echec(kwargs,
                                  erreur,
                                  message_erreur):

    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Utilisateur.nombre_observation(kwargs)


# # Définition des cas de test pour nombre_observation réussie
# @pytest.mark.parametrize(
#     'kwargs_str',
#     [
#         'station_kwargs'
#     ]
# )
# def test_station_nombre_observation_succes(kwargs_str, request):
#     kwargs = request.getfixturevalue(kwargs_str)
#     Utilisateur.nombre_observation(kwargs)

# Définition des cas de test pour calcul_totaux_statut échec

# @pytest.mark.parametrize(
#     'kwargs, erreur, message_erreur',
#     [
#         ({2, "str"}, TypeError,
#          "La base de données doit être un DataFrame.")

#     ]
# )
# def test_calcul_totaux_statut_echec(utilisateur_kwargs,
#                                     kwargs,
#                                     erreur,
#                                     message_erreur):
#     utilisateur_kwargs.update(kwargs)
#     with pytest.raises(erreur, match=re.escape(message_erreur)):
#         Utilisateur(**utilisateur_kwargs)
