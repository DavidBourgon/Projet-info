# %% Installe les dépendances et lance l'interface
import os
import webbrowser
from particulier import Particulier 

if __name__ == "__main__":
    os.system('pip install -r requirements.txt')

    path = os.path.abspath("interface.html")

    webbrowser.open("file://" + path)

# %% Ici des exemples d'applications des fonctions pour
# la classe Secteur_privé

from secteur_prive import SecteurPrive

import pandas as pd

# Import des donnée

data = pd.read_excel("Bronx_sans_Na.xlsx")

# Création de deux assureurs différents ayant des marges différentes :

Groupama = SecteurPrive("Groupama", 0.5)
Axa = SecteurPrive("AXA", 0.8)


# Renvoie combien va payer un Client de l'assureur
# pour son trajet le plus fréquent

# D'abord si ce dernier se déplace en voiture ainsi que le type de véhicule

# Chez Groupama
print(Groupama.__repr__(data, "1 E 161st St, Bronx, NY 10451, États-Unis",
                        "111 E 164th St, Bronx, NY 10452, États-Unis",
                        "car", "Pick-up Truck"))

# Chez Axa
print(Axa.__repr__(data, "1 E 161st St, Bronx, NY 10451, États-Unis",
                         "111 E 164th St, Bronx, NY 10452, États-Unis",
                         "car", "Pick-up Truck"))

# Lorsque le client se déplace en vélo

print(Groupama.__repr__(data, "1 E 161st St, Bronx, NY 10451, États-Unis",
                        "111 E 164th St, Bronx, NY 10452, États-Unis",
                        "cycle"))

# Chez Axa
print(Axa.__repr__(data, "1 E 161st St, Bronx, NY 10451, États-Unis",
                         "111 E 164th St, Bronx, NY 10452, États-Unis",
                         "cycle"))

# %% Ici des exemples d'applications des fonctions pour
# la classe Particulier


# from secteur_prive import SecteurPrive

# import pandas as pd

# # Import des donnée

# data = pd.read_excel("Bronx_sans_Na.xlsx")

# Xavier = Particulier("car", "08:00")
# print(Xavier.eviter_zone_risquee("1 E 161st St, Bronx, NY 10451, États-Unis",
#                                  "111 E 164th St, Bronx, NY 10452, "
#                                  "États-Unis"))







print(Groupama.__repr__(data, "Heath Avenue, Bronx, New York",
                        "Heath Avenue, Bronx, New York",
                        "cycle"))
