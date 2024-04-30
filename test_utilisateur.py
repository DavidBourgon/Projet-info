from utilisateur import Utilisateur
import pytest
import re


# Définition des cas de test pour nombre_observation échec
@pytest.mark.parametrize(
    'kwargs, erreur, message_erreur',
    [
        ({2}, TypeError,
         "La base de données doit être un DataFrame.")
    ]
)
def test_nombre_observation_echec(utilisateur_kwargs,
                                  kwargs,
                                  erreur,
                                  message_erreur):
    utilisateur_kwargs.update(kwargs)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Utilisateur(**utilisateur_kwargs)


# Définition des cas de test pour nombre_observation réussie
@pytest.mark.parametrize(
    'kwargs_str',
    [
        'station_kwargs'
    ]
)
def test_station_nombre_observation_succes(kwargs_str, request):
    kwargs = request.getfixturevalue(kwargs_str)
    Utilisateur(**kwargs)

# BROUILLON NE PAS TOUCHER !!!

# Définition des cas de test pour la méthode nombre_observation échec
@pytest.mark.parametrize(
    'kwargs, data, erreur, message_erreur',
    [
        ({}, 60, TypeError,
         "La base de données doit être un DataFrame.")
    ]
)
def test_nombre_observation_echec(obs_kwargs, kwargs, data,
                                  erreur, message_erreur):
    obs_kwargs.update(kwargs)
    utilisateur = Utilisateur(**obs_kwargs)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        utilisateur.nombre_observation(data)


# Définition des cas de test pour la méthode nombre_observation succés
@pytest.mark.parametrize(
    'kwargs, nom_carburant, erreur, message_erreur',
    [
        ({}, 60, TypeError,
         "Le nom de carburant doit être une chaîne de caractères."),
        ({"pompes": {"SP98": pytest.pompe_gpl},
          "prix": {"SP98": 1.5}}, 'SP98', ValueError,
         "Le carburant ne correspond pas au nom de la pompe"),
    ]
)
def test_station_verif_pompe(station_kwargs, kwargs, nom_carburant,
                             erreur, message_erreur):
    station_kwargs.update(kwargs)
    station = Station(**station_kwargs)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        station._Station__verifier_pompe(nom_carburant)
