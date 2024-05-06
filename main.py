# %% Installe les dépendances et lance l'interface
import os
import webbrowser

if __name__ == "__main__":
    os.system('pip install -r requirements.txt')

    path = os.path.abspath("interface.html")

    webbrowser.open("file://" + path)

# %% Ici des exemples d'applications des fonctions
