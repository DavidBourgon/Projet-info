# %% Installe les dépendances et lance l'interface
import os
import webbrowser

if __name__ == "__main__":
    os.system('pip install -r requirements.txt')

    path = os.path.abspath("interface.html")

    webbrowser.open("file://" + path)

# %% Ici des exemples d'applications des fonctions

from secteur_prive import SecteurPrive
from particulier import Particulier
from secteur_public import SecteurPublic

Xavier = Particulier("car", "08:00")
print(Xavier.eviter_zone_risquee("1 E 161st St, Bronx, NY 10451, États-Unis",
                                 "111 E 164th St, Bronx, NY 10452, "
                                 "États-Unis"))

data = pd.read_excel("Bronx_sans_Na.xlsx")
Groupama = SecteurPrive("Groupama", 0.5)

# print(Groupama.__repr__(data, "1 E 161st St, Bronx, NY 10451, États-Unis",
#                         "111 E 164th St, Bronx, NY 10452, États-Unis",
#                         "car"))

#print(SecteurPrive.risque_rue_naif(data, 'HEATH AVENUE', 'cycle'))

print(Groupama.__repr__(data, "Heath Avenue, Bronx, New York",
                        "Heath Avenue, Bronx, New York",
                        "cycle"))

