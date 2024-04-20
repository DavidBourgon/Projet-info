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


# data = pd.read_excel("Bronx_2.xlsx")
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

# data = pd.read_excel("Bronx_2.xlsx")
# street = 'HEATH AVENUE'
# print(nmbr_blessés_total_rue(data, street))
