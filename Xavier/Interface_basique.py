#%% importation des modules
# from Utilisateur import Utilisateur
# from secteur_prive import SecteurPrive
# from secteur_public import SecteurPublic
# from particulier import Particulier
import tkinter as tk
import time


def choisi(L):
    mot = input("Entrez votre réponse :")
    while mot not in L:
        print(f"{mot} n'est pas conforme ou bien orthographier")
        exemple = " ou ".join(L)
        print(f"Vous devez renseigner soit : {exemple}")
        time.sleep(1)
        mot = input("Entrez de nouveau votre réponse : ")
    print("Votre réponse est correcte")
    return mot

#%% Corps de l'application


try:
    # Se lance automatiquement qd on exécute le fichier
    print("Bienvenue dans vie de quartier")
    time.sleep(2)
    print("L'application qui te renseigne sur les dangers dans ton quartier")
    time.sleep(1)
    print("Quel profil d'utilisateur êtes vous ?")
    time.sleep(1)

    choix = choisi(["Secteur Privé", "Secteur Public", "Particulier"])

    time.sleep(1)

    if choix == "Secteur Privé":
        print("En tant qu'acteur privé que souhaitez vous faire ?")
        time.sleep(1)

    elif choix == "Secteur Public":
        print("En tant qu'acteur public que souhaitez vous faire ?")
        time.sleep(1)

    elif choix == "Particulier":
        print("En tant que particulier que souhaitez vous faire ?")
        time.sleep(1)


except KeyboardInterrupt:
    # faire CTRL C pour fermer l'application
    print()
    print("Fermeture de l'application")
    time.sleep(1)
    print("Nous espérons bientôt vous revoir !!!")
