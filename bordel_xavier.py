# pip install openpyxl
# pip install pandas

import pandas as pd


data = pd.read_excel("BdD_Bronx.xlsx")


def nmbr_mort_total(data):
    # Calculer le nombre total de personnes tuées
    total_persons_killed = data["NUMBER.OF.PERSONS.KILLED"].sum()
    return ("Nombre total de personnes tuées dans toute la base de données :",
            total_persons_killed)

# result = nmbr_mort_total(data)
# print(result)


def nmbr_mort_total_rue(data, street: str):
    # Calculer le nombre total de personnes par rue
    total_persons_killed = data.groupby(street)["NUMBER.OF.PERSONS.KILLED"].sum()
    return ("Nombre total de personnes tuées dans la rue base de données :",
            total_persons_killed)


street = 'HEATH AVENUE'
print(nmbr_mort_total_rue(data, street))
