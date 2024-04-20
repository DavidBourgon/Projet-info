# pip install openpyxl
# pip install pandas

import pandas as pd


data = pd.read_excel("Bronx_2.xlsx")


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
    return ("Nombre total de personnes bléssées dans toute la base de données :",
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
    total_persons_injuried_street = street_data["NUMBER.OF.PERSONS.INJURED"].sum()
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
    list: Liste des modalités différentes de la variable "CONTRIBUTING.FACTOR.VEHICLE.1".
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
            "et la variable",
            variable,
            filtered_data)


# modalité = "Unspecified"
# variable = "CONTRIBUTING.FACTOR.VEHICLE.1"
# print(filtrer_par_modalité(data, variable, modalité))
