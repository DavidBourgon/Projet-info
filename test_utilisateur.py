from Utilisateur import Utilisateur
import pytest
import pandas as pd
import re

tableau = pd.read_excel("Bronx_2.xlsx")


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
# MArcherais si il y avait un self
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


# Définition des cas de test pour calcul_totaux_statut échec
@pytest.mark.parametrize(
    'data, statut, erreur, message_erreur',
    [
        (3, "str", TypeError,
         "La base de données doit être un DataFrame."),
        (tableau, 4, TypeError,
         "Le statut doit être de type str."),
        (tableau, "statut", ValueError,
         "Le statut doit être B, T ou BT.")
    ]
)
def test_calcul_totaux_statut_echec(data,
                                    statut,
                                    erreur,
                                    message_erreur):

    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Utilisateur.calcul_totaux_statut(data, statut)


# Définition des cas de test pour calcul_totaux_cat_statut échec
@pytest.mark.parametrize(
    'data, categorie, statut, erreur, message_erreur',
    [
        (3, "cat", "str", TypeError,
         "La base de données doit être un DataFrame."),

        (tableau, "cat", 4, TypeError,
         "Le statut doit être de type str."),
        (tableau, "cat", "statut", ValueError,
         "Le statut doit être B, T ou BT."),

        (tableau, 2, "B", TypeError,
         "La catégorie doit être de type str."),
        (tableau, "cat", "B", ValueError,
         "La catégorie doit être car, cycle ou foot."),
    ]
)
def test_calcul_totaux_cat_statut_echec(data,
                                        categorie,
                                        statut,
                                        erreur,
                                        message_erreur):

    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Utilisateur.calcul_totaux_cat_statut(data, categorie, statut)


# Définition des cas de test pour filtrer_par_nom_de_rue échec
@pytest.mark.parametrize(
    'data, street, erreur, message_erreur',
    [
        (3, "str", TypeError,
         "La base de données doit être un DataFrame."),

        (tableau, 4, TypeError,
         "Le nom de la rue doit être de type str."),
        (tableau, "rue", ValueError,
         "Le nom de la rue doit contenir uniquement"
         " des majuscules et des espaces"),

    ]
)
def test_filtrer_par_nom_de_rue_echec(data,
                                      street,
                                      erreur,
                                      message_erreur):

    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Utilisateur.filtrer_par_nom_de_rue(data, street)


# Définition des cas de test pour filtrer_par_date() échec
@pytest.mark.parametrize(
    'data, date_debut, date_fin, erreur, message_erreur',
    [
        (3, "str", "str", TypeError,
         "La base de données doit être un DataFrame."),

        (tableau, 4, "str", TypeError,
         "La date début doit être un str."),
        (tableau, "17/01/2021", "str", ValueError,
         "La date début doit être au format 'MM/JJ/AAAA'."),

        (tableau, "01/31/2021", 4, TypeError,
         "La date fin doit être un str."),
        (tableau, "01/31/2021", "17/01/2021", ValueError,
         "La date fin doit être au format 'MM/JJ/AAAA'."),

        (tableau, "01/31/2021", "01/17/2021", ValueError,
         "La date de début ne doit pas être supérieure"
         " à la date de fin."),

    ]
)
def test_filtrer_par_date_echec(data,
                                date_debut,
                                date_fin,
                                erreur,
                                message_erreur):

    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Utilisateur.filtrer_par_date(data, date_debut, date_fin)


# Définition des cas de test pour filtrer_par_heure() échec
@pytest.mark.parametrize(
    'data, heure_debut, heure_fin, erreur, message_erreur',
    [
        (3, "str", "str", TypeError,
         "La base de données doit être un DataFrame."),

        (tableau, 4, "str", TypeError,
         "L'heure de début doit être un str"),
        (tableau, "8:00", "str", ValueError,
         "L'heure de début doit être au format 'HH:MM'."),

        (tableau, "08:00", 4, TypeError,
         "L'heure de fin doit être un str"),
        (tableau, "08:00", "8:00", ValueError,
         "L'heure de fin doit être au format 'HH:MM'."),

        (tableau, "08:00", "07:00", ValueError,
         "L'heure de début ne doit pas être supérieure"
         " à l'heure de fin."),
    ]
)
def test_filtrer_par_heure_echec(data,
                                 heure_debut,
                                 heure_fin,
                                 erreur,
                                 message_erreur):

    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Utilisateur.filtrer_par_heure(data, heure_debut, heure_fin)


# Définition des cas de test pour filtrer_par_modalite_variable() échec
@pytest.mark.parametrize(
    'data, variable, modalite, erreur, message_erreur',
    [
        (3, "str", "str", TypeError,
         "La base de données doit être un DataFrame."),

        (tableau, "A.B.C", "str", ValueError,
         "Cette variable n'est pas dans la base de données."),

        (tableau, "CRASH.TIME", "str", ValueError,
         "Cette modalité n'existe pas pour la variable choisie."),
    ]
)
def test_filtrer_par_modalite_variable_echec(data,
                                             variable,
                                             modalite,
                                             erreur,
                                             message_erreur):

    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Utilisateur.filtrer_par_modalite_variable(data, variable, modalite)


# Définition des cas de test pour liste_variables_dataframe échec
@pytest.mark.parametrize(
    'data, erreur, message_erreur',
    [
        (2, TypeError,
         "La base de données doit être un DataFrame.")
    ]
)
def test_liste_variables_dataframe_echec(data,
                                         erreur,
                                         message_erreur):

    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Utilisateur.liste_variables_dataframe(data)


# Définition des cas de test pour liste_modalites_variable échec
@pytest.mark.parametrize(
    'data, variable, erreur, message_erreur',
    [
        (2, "str", TypeError,
         "La base de données doit être un DataFrame."),
        (tableau, 4, TypeError,
         "La variable doit être de type str."),

        (tableau, "str", ValueError,
         "La variable ne doit contenir que "
         "des majuscules, des points, des nombres "
         "et pas d'espace."),

        (tableau, "A.B.C", ValueError,
         "Cette variable n'est pas dans la base de données."),
    ]
)
def test_liste_modalites_variable_echec(data,
                                        variable,
                                        erreur,
                                        message_erreur):

    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Utilisateur.liste_modalites_variable(data, variable)

@pytest.mark.parametrize(
    'kwargs_str',
    [
        'carburant_gazole_kwargs', 'sp98_kwargs', 'sp95_kwargs',
        'sp95_e10_kwargs', 'e85_kwargs', 'gpl_kwargs'
    ]
)
def test_calcul_totaux_statut(kwargs_str, request):
    kwargs = request.getfixturevalue(kwargs_str)
    Carburant(**kwargs)