# %% Ici des exemples d'applications des fonctions pour
import pandas as pd
# la classe Secteur_privé

# Import des donnée
data = pd.read_excel("Bronx_sans_Na.xlsx")
from secteur_prive import SecteurPrive
# Création de deux assureurs différents ayant des marges différentes :
Groupama = SecteurPrive("Groupama", 0.5)
Axa = SecteurPrive("AXA", 0.8)

# Renvoie combien va payer un Client de l'assureur
# pour son trajet le plus fréquent
# Si ce dernier se déplace en voiture ainsi que le type de véhicule
# Chez Groupama
print(Groupama.__repr__(data, "1818 Archer St, Bronx, NY",
                        "1775 Mansion St, Bronx, NY",
                        "car", "Sedan"))

# Chez Axa
print(Axa.__repr__(data,"1818 Archer St, Bronx, NY",
                        "1775 Mansion St, Bronx, NY",
                        "car", "Sedan"))

# Lorsque le client se déplace en vélo
# Chez Groupama
print(Groupama.__repr__(data, "1818 Archer St, Bronx, NY",
                        "1775 Mansion St, Bronx, NY",
                        "cycle"))

# Chez Axa
print(Axa.__repr__(data, "1818 Archer St, Bronx, NY",
                   "1775 Mansion St, Bronx, NY",
                   "cycle"))
