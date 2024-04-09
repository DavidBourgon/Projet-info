# pip install openpyxl
# pip install pandas

import pandas as pd


data = pd.read_excel("BdD_Bronx.xlsx")


def nmbr_mort_total():
    # Calculer le nombre total de personnes tuées
    total_persons_killed = data["NUMBER.OF.PERSONS.KILLED"].sum()
    return ["Nombre total de personnes tuées dans toute la base de données :",
            total_persons_killed]

