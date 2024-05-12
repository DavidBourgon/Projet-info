# %% Installe les dépendances et lance l'interface
import os

os.system('pip install -r requirements.txt')

from particulier import Particulier


# %% Ici des exemples d'applications des fonctions pour
# la classe Particulier

# Création de deux particliers différents ayant
# des moyens de locomotion différents et heure de départ différents
John = Particulier("car", "08:00")

print(John.eviter_zone_risquee("1818 Archer St, Bronx, NY",
                               "1928 Benedict Ave, Bronx, NY"))
