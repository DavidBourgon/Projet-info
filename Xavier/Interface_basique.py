#%% importation des modules
# from Utilisateur import Utilisateur
# from secteur_prive import SecteurPrive
# from secteur_public import SecteurPublic
# from particulier import Particulier
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

#%% Corps de l'application


try:
    print("Bienvenue dans vie de quartier")
    time.sleep(2)
    print("L'application qui te renseigne sur les dangers dans ton quartier")
    time.sleep(1)
    print("Quel profil d'utilisateur êtes vous ?")
    time.sleep(1)

    choisi(["Secteur Privé", "Secteur Public", "Particulier"])

    time.sleep(1)

    if mot == "Secteur Privé":
        print("En tant qu'acteur privé que souhaitez vous faire ?")
        time.sleep(1)

    elif mot == "Secteur Public":
        print("En tant qu'acteur public que souhaitez vous faire ?")
        time.sleep(1)

    elif mot == "Particulier":
        print("En tant que particulier que souhaitez vous faire ?")
        time.sleep(1)


except KeyboardInterrupt:
    print("Fermeture de l'application")
    time.sleep(1)
    print("Nous espérons bientôt vous revoir !!!")
