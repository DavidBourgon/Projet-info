from station import Station
import pytest
import re


# Définition des cas de test pour l'initialisation invalide
@pytest.mark.parametrize(
    'kwargs, erreur, message_erreur',
    [
        ({'pompes': 2}, TypeError,
         "Les pompes sont des dictionnaires."),
        ({'pompes': {1: pytest.pompe_gpl}}, TypeError,
         "Les clés du dictionnaire doivent être de type str"),
        ({'pompes': {'clef': 4}}, TypeError,
         "Les valeurs du dictionnaire doivent être de type Pompe"),


        ({'prix': 1}, TypeError,
         ("Les prix sont des dictionnaires")),
        ({'prix': {2: 'valeurs'}}, TypeError,
         ("Les clés du dictionnaire doivent être de type str")),
        ({'prix': {'clef': 'valeurs'}}, ValueError,
         ("Les valeurs du dictionnaire doivent être de type float")),

        ({'prix': {'clef': -0.4}}, ValueError,
         ("La valeur de prix ne doit pas être négative.")),
        ({'prix': {'clef1': 10.0},
          'pompes': {'clef2': pytest.pompe_gpl}},
         ValueError, ("Les clés des carburants dans les pompes"
                      " doivent correspondre aux clés des prix.")),

    ]
)
def test_station_init_echec(station_kwargs,  kwargs, erreur, message_erreur):
    station_kwargs.update(kwargs)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Station(**station_kwargs)


# Définition des cas de test pour l'initialisation réussie
@pytest.mark.parametrize(
    'kwargs_str',
    [
        'station_kwargs'
    ]
)
def test_station_init_succes(kwargs_str, request):
    kwargs = request.getfixturevalue(kwargs_str)
    Station(**kwargs)


# Définition des cas de test pour la méthode _verifier_nom_carburant
@pytest.mark.parametrize(
    'kwargs, nom_carburant, erreur, message_erreur',
    [
        ({}, 60, TypeError,
         "Le nom de carburant doit être une chaîne de caractères."),
        ({"pompes": {"pompe_gpl": pytest.pompe_gpl},
          "prix": {"pompe_gpl": 1.5}}, 'str', ValueError,
         "Le carburant n'est pas disponible dans la station."),
    ]
)
def test_station_verif_nom_carburant(station_kwargs, kwargs, nom_carburant,
                                     erreur, message_erreur):
    station_kwargs.update(kwargs)
    station = Station(**station_kwargs)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        station._Station__verifier_nom_carburant(nom_carburant)


# Définition des cas de test pour la méthode _verifier_pompe
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
