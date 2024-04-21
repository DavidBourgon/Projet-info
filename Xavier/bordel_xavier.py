# pip install openpyxl
# pip install pandas

import pandas as pd
data = pd.read_excel("Bronx_2.xlsx")


def nombre_observation(data):
    """
    Compte le nombre d'observations dans un DataFrame.

    Args:
    data (DataFrame): Le DataFrame contenant les données.

    Returns:
    int: Nombre d'observations dans le DataFrame.

    Raises:
    TypeError: Si data n'est pas un DataFrame.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data de nombre_observation doit être un DataFrame.")

    return ("Nombre d'observations dans le DataFrame :", data.shape[0])


# print(nombre_observation(data))


def nmbr_mort_total(data):
    # Calculer le nombre total de personnes tuées
    total_persons_killed = data["NUMBER.OF.PERSONS.KILLED"].sum()
    return ("Nombre total de personnes tuées dans toute la base de données :",
            total_persons_killed)

# result = nmbr_mort_total(data)
# print(result)


def nmbr_blessés_total(data):
    # Calculer le nombre total de personnes tuées
    total_persons_injuried = data["NUMBER.OF.PERSONS.INJURED"].sum()
    return ("Nombre total de personnes bléssées dans toute la base :",
            total_persons_injuried)

# result = nmbr_blessés_total(data)
# print(result)


def nmbr_mort_total_rue(data, street: str):
    # Calculer le nombre total de personnes par rue
    street_data = data[data["CROSS.STREET.NAME"].str.contains(street) |
                       data["ON.STREET.NAME"].str.contains(street) |
                       data["OFF.STREET.NAME"].str.contains(street)]
    total_persons_killed_street = street_data["NUMBER.OF.PERSONS.KILLED"].sum()
    return ("Nombre total de personnes tuées dans la rue base de données :",
            total_persons_killed_street)

# street = 'HEATH AVENUE'
# print(nmbr_mort_total_rue(data, street))


def nmbr_blessés_total_rue(data, street: str):
    # Calculer le nombre total de personnes par rue
    street_data = data[data["CROSS.STREET.NAME"].str.contains(street) |
                       data["ON.STREET.NAME"].str.contains(street) |
                       data["OFF.STREET.NAME"].str.contains(street)]
    total_persons_injuried_street = street_data["NUMBER.OF.PERSONS.INJURED"].\
        sum()
    return ("Nombre total de personnes bléssées dans la rue base de données :",
            total_persons_injuried_street)

# street = 'HEATH AVENUE'
# print(nmbr_blessés_total_rue(data, street))


def total_piétons_blessés_tués(data):
    colonnes_piétons = ["NUMBER.OF.PEDESTRIANS.INJURED",
                        "NUMBER.OF.PEDESTRIANS.KILLED"]
    total_piétons = data[colonnes_piétons].sum().sum()
    return ("Nombre total de piétons blessés ou tués :",
            total_piétons)

# total_piétons = total_piétons_blessés_tués(data)
# print(total_piétons)
# print(total_piétons_blessés_tués(data))


def total_cyclistes_blessés_tués(data):
    colonnes_cyclistes = ["NUMBER.OF.CYCLIST.INJURED",
                          "NUMBER.OF.CYCLIST.KILLED"]
    total_cyclistes = data[colonnes_cyclistes].sum().sum()
    return ("Nombre total de cyclistes blessés ou tués :",
            total_cyclistes)

# print(total_cyclistes_blessés_tués(data))


def total_automobilistes_blessés_tués(data):
    colonnes_automobilistes = ["NUMBER.OF.MOTORIST.INJURED",
                               "NUMBER.OF.MOTORIST.KILLED"]
    total_automobilistes = data[colonnes_automobilistes].sum().sum()
    return ("Nombre total d'automobilistes blessés ou tués :",
            total_automobilistes)

# print(total_automobilistes_blessés_tués(data))


def modalités_variable(data, variable):
    """
    Renvoie toutes les modalités différentes d'une variable
    dans une liste.

    attention varible en majusccule et séparéles mots par des points
    Args:
    data (DataFrame): Le DataFrame contenant les données.

    Returns:
    list: Liste des modalités différentes de la variable.
    """
    return ("Modalités différentes de :",
            variable,
            list(data[variable].unique()))


# variable = "CONTRIBUTING.FACTOR.VEHICLE.1"
# print(modalités_variable(data, variable))


def filtrer_par_modalité(data, variable, modalité):
    """
    Filtre le DataFrame en fonction d'une modalité spécifique d'une variable
    spécifique et renvoie le DataFrame filtré.

    Args:
    data (DataFrame): Le DataFrame contenant les données.
    modalité (str): La modalité spécifique à filtrer.

    Returns:
    DataFrame: Le DataFrame filtré.
    """
    filtered_data = data[data[variable] == modalité]
    return ("Data frame filtré pour la modalité",
            modalité,
            "de la variable",
            variable,
            filtered_data)


# modalité = "Unspecified"
# variable = "CONTRIBUTING.FACTOR.VEHICLE.1"
# print(filtrer_par_modalité(data, variable, modalité))


def filtrer_par_date(data, date_debut, date_fin):
    """
    Filtre le DataFrame en fonction de la date entre date_debut et date_fin
    inclusivement.

    Args:
    data (DataFrame): Le DataFrame contenant les données.
    date_debut (str): La date de début de la période choisie au format
    "MM/DD/YYYY".
    date_fin (str): La date de fin de la période choisie au format
    "MM/DD/YYYY".

    Returns:
    DataFrame: Le DataFrame filtré.
    """
    # Convertir les colonnes "CRASH.DATE" en type datetime
    data["CRASH_DATE"] = pd.to_datetime(data["CRASH.DATE"])

    # Les bornes sont prises
    filtered_data = data[(data["CRASH_DATE"] >= pd.to_datetime(date_debut)) &
                         (data["CRASH_DATE"] <= pd.to_datetime(date_fin))]

    # Supprimer la colonne temporaire "CRASH_DATE"
    filtered_data = filtered_data.drop(columns=["CRASH_DATE"])

    return ("Data frame filtré pour la période du",
            date_debut,
            "au",
            date_fin,
            filtered_data)


# # Année 2021
# date_debut = "01/01/2021"
# date_fin = "12/31/2021"
# print(filtrer_par_date(data, date_debut, date_fin))


def filtrer_par_heure(data, heure_debut, heure_fin):
    """
    Filtre le DataFrame en fonction de l'heure entre heure_debut
    et heure_fin inclusivement.

    Args:
    data (DataFrame): Le DataFrame contenant les données.
    heure_debut (str): L'heure de début de la période au format "HH:MM".
    heure_fin (str): L'heure de fin de la période au format "HH:MM".

    Returns:
    tuple: Un tuple contenant un message décrivant la période filtrée
    et le DataFrame filtré.
    """
    # Convertir les colonnes "CRASH.TIME" en type datetime
    data["CRASH_TIME"] = pd.to_datetime(data["CRASH.TIME"]).dt.\
        strftime("%H:%M")

    # Filtrer le DataFrame en fonction de l'heure entre heure_debut
    # et heure_fin inclusivement
    filtered_data = data[(data["CRASH_TIME"] >= heure_debut) &
                         (data["CRASH_TIME"] <= heure_fin)]

    # Supprimer la colonne temporaire "CRASH_TIME"
    filtered_data = filtered_data.drop(columns=["CRASH_TIME"])

    return ("Data frame filtré pour la période entre",
            heure_debut,
            "et",
            heure_fin, ":",
            filtered_data)

# # Définir les heures de début et de fin de la période choisie
# heure_debut = "08:00" # attention ne prends pas 24:00 s'arrête à 00:01
# heure_fin = "08:40" # attention ne prends pas 24:00 s'arrête à 23:59
# print(filtrer_par_heure(data, heure_debut, heure_fin))
