import pandas as pd

# Création d'un DataFrame exemple
data = pd.read_excel("BdD_Bronx.xlsx")

# Filtrage du DataFrame
df_filtré = data[data["CROSS.STREET.NAME"].isna()]
