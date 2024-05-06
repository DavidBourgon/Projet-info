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


# Définition des cas de test pour nombre_observation succes
@pytest.mark.parametrize(
    'data, resultat_attendu',
    [

     (tableau, ["Nombre d'observations dans la base de données :", 2000])

    ]
)
def test_nombre_observation_sucess(data, resultat_attendu):
    assert (
        Utilisateur.nombre_observation(data)
        ==
        resultat_attendu
    )


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


# Définition des cas de test pour calcul_totaux_statut succes
@pytest.mark.parametrize(
    'data, statut, resultat_attendu',
    [

     (tableau, "B", ["Nombre total d'individus blessés :", 846]),
     (tableau, "T", ["Nombre total d'individus tués :", 4]),
     (tableau, "BT", ["Nombre total d'individus blessés et tués :", 850]),

    ]
)
def test_calcul_totaux_statut_sucess(data, statut, resultat_attendu):
    assert (
        Utilisateur.calcul_totaux_statut(data, statut)
        ==
        resultat_attendu
    )


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


# Définition des cas de test pour calcul_totaux_cat_statut succes
@pytest.mark.parametrize(
    'data, categorie, statut, resultat_attendu',
    [

     (tableau, "foot", "B", ['Nombre total de piétons blessés :', 151]),
     (tableau, "foot", "T", ['Nombre total de piétons tués :', 0]),
     (tableau, "foot", "BT", ['Nombre total de piétons blessés et tués :',
                              151]),

     (tableau, "car", "B", ["Nombre total d'automobilistes blessés :", 592]),
     (tableau, "car", "T", ["Nombre total d'automobilistes tués :", 2]),
     (tableau, "car", "BT", ["Nombre total d'automobilistes blessés et tués :",
                             594]),

     (tableau, "cycle", "B", ['Nombre total de cyclistes blessés :', 65]),
     (tableau, "cycle", "T", ['Nombre total de cyclistes tués :', 1]),
     (tableau, "cycle", "BT", ['Nombre total de cyclistes blessés et tués :',
                               66]),

    ]
)
def test_calcul_totaux_cat_statut_sucess(data, categorie, statut,
                                         resultat_attendu):
    assert (
        Utilisateur.calcul_totaux_cat_statut(data, categorie, statut)
        ==
        resultat_attendu
    )


# Définition des cas de test pour filtrer_par_nom_de_rue échec
@pytest.mark.parametrize(
    'data, street, erreur, message_erreur',
    [
        (3, "str", TypeError,
         "La base de données doit être un DataFrame."),

        (tableau, 4, TypeError,
         "Le nom de la rue doit être de type str.")

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


# Définition des cas de test pour liste_variables_dataframe succes
@pytest.mark.parametrize(
    'data, resultat_attendu',
    [

     (tableau, ['Liste des variables de la base de données :',
                ['CRASH.DATE', 'CRASH.TIME',
                 'BOROUGH', 'ZIP.CODE',
                 'LATITUDE', 'LONGITUDE', 'LOCATION',
                 'ON.STREET.NAME', 'CROSS.STREET.NAME', 'OFF.STREET.NAME',
                 'NUMBER.OF.PERSONS.INJURED', 'NUMBER.OF.PERSONS.KILLED',

                 'NUMBER.OF.PEDESTRIANS.INJURED',
                 'NUMBER.OF.PEDESTRIANS.KILLED',
                 'NUMBER.OF.CYCLIST.INJURED',
                 'NUMBER.OF.CYCLIST.KILLED',
                 'NUMBER.OF.MOTORIST.INJURED',
                 'NUMBER.OF.MOTORIST.KILLED',

                 'CONTRIBUTING.FACTOR.VEHICLE.1',
                 'CONTRIBUTING.FACTOR.VEHICLE.2',
                 'CONTRIBUTING.FACTOR.VEHICLE.3',
                 'CONTRIBUTING.FACTOR.VEHICLE.4',
                 'CONTRIBUTING.FACTOR.VEHICLE.5',

                 'COLLISION_ID',
                 'VEHICLE.TYPE.CODE.1',
                 'VEHICLE.TYPE.CODE.2',
                 'VEHICLE.TYPE.CODE.3',
                 'VEHICLE.TYPE.CODE.4',
                 'VEHICLE.TYPE.CODE.5']])

    ]
)
def test_liste_variables_dataframe_sucess(data, resultat_attendu):
    assert (
        Utilisateur.liste_variables_dataframe(data)
        ==
        resultat_attendu
    )


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


# Définition des cas de test pour liste_modalites_variable succes
@pytest.mark.parametrize(
    'data, variable, resultat_attendu',
    [

     (tableau, "VEHICLE.TYPE.CODE.2",
      ['Liste des modalités différentes de la variable :',
       "VEHICLE.TYPE.CODE.2",
       ['Sedan', 'nan', 'Station Wagon/Sport Utility Vehicle',
        'Bike', 'Refrigerated Van', 'E-Bike', 'Ambulance',
        'Taxi', 'Bus', 'Pick-up Truck', 'Tractor Truck Diesel',
        'Box Truck', 'Garbage or Refuse', 'Motorcycle', 'Moped',
        'E-Scooter', 'MOPED', 'Van', 'UNK', 'Concrete Mixer',
        'PK', 'FIRE TRUCK', 'Carry All', 'Motorscooter',
        'Flat Bed', 'FORKLIFT', 'AMBULANCE', 'UNKNOWN',
        'TRK', 'AMBU', 'FDNY FIRET', 'ESCOOTER S',
        'Convertible', 'FORK LIFT', 'Tow Truck / Wrecker',
        'Motorbike', 'TOW TRUCK', '4 dr sedan', 'Dump', 'Pick up',
        '3-Door', 'ambulance']])

    ]
)
def test_liste_modalites_variable_sucess(data, variable, resultat_attendu):
    assert (
        Utilisateur.liste_modalites_variable(data, variable)
        ==
        resultat_attendu
    )


tableau2 = pd.DataFrame(columns=["colonne1", "colonne2", "colonne3"])


# Définition des cas de test pour risque_rue succes
@pytest.mark.parametrize(
    'data, street, categorie, resultat_attendu',
    [

     (tableau, "HEATH AVENUE", 'foot',
      ["Pour la rue :", "HEATH AVENUE",
       "il y a un rique (en %) de :", 0.0]),
    ]
)
def test_risque_rue_sucess(data, street, categorie, resultat_attendu):
    assert (
        Utilisateur.risque_rue(data, street, categorie)
        ==
        resultat_attendu
    )
