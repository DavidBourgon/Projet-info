#%% importation des modules
import pandas as pd
import tkinter as tk
import time
# from particulier import Particulier
# from secteur_prive import SecteurPrive
# from Utilisateur import Utilisateur

tableau = pd.read_excel("Bronx_2.xlsx")

def choisi(L):
    mot = input("Entrez votre réponse :")
    while mot not in L:
        print(f"{mot} n'est pas conforme ou pas bien orthographié.")
        exemple = " ou ".join(L)
        print(f"Vous devez renseigner soit : {exemple}")
        time.sleep(1)
        mot = input("Entrez de nouveau votre réponse : ")
    print("Votre réponse est correcte.")
    return mot

#%% Corps de l'application


try:
    # Se lance automatiquement qd on exécute le fichier
    print("Bienvenue dans vie de quartier.")
    time.sleep(2)
    print("L'application qui te renseigne sur les dangers dans ton quartier.")
    time.sleep(1)
    print("Quel profil d'utilisateur êtes vous ?")
    time.sleep(1)

    choix = choisi(["Secteur Privé", "Secteur Public", "Particulier"])

    time.sleep(1)

    if choix == "Secteur Privé":
        print("En tant qu'acteur privé que souhaitez vous faire ?")
        time.sleep(1)

        utilisation = choisi(["Déterminer le prix de mon assurance."])
        time.sleep(1)

        if utilisation == "Déterminer le prix de mon assurance.":
            print("Quel véhicule souhaitez vous assurer ?")
            time.sleep(1)

            vehicule = choisi([])

            print("Entrez une liste de localisations que vous fréquentez "
                  "régulièrement.")

            localisation = choisi([])
            time.sleep(1)
            print("Le prix de votre assurance sera de :",
                  self.__donner_prix(data, localisation, vehicule))

    elif choix == "Secteur Public":
        print("En tant qu'acteur public que souhaitez vous faire ?")
        time.sleep(1)

        utilisation = choisi(["Connaître le taux de mortalité d'une rue.",
                              "Localiser une infrastructure."])
        time.sleep(1)

        if utilisation == "Connaître le taux de mortalité d'une rue.":
            print("Sur quelle rue souhaitez vous connaître le taux de mortalité ?")
            time.sleep(1)

            rue = input("Entrez le nom de la rue, doit finir par ', New York' :")

    elif choix == "Particulier":
        print("En tant que particulier que souhaitez vous faire ?")
        time.sleep(1)

        utilisation = choisi(["Connaître le risque d'un itinéraire.",
                              "Savoir quel moyen de transport utiliser pour"
                              " éviter les risques et avoir l'itinéraire correspondant."])
        time.sleep(1)

        if utilisation == "Connaître le risque d'un itinéraire.":
            print("Quelle est votre adresse de départ ?")
            adresse_depart = input("Entrez le nom de la rue, doit finir par ', New York' :")

            time.sleep(1)
            print("Quelle est votre adresse d'arrivée ?")
            adresse_arrivee = input("Entrez le nom de la rue, doit finir par ', New York' :")

            time.sleep(1)
            print("Voici le risque de l'itinéraire permettant de relier vos 2 adresses :",
                  Particulier.evaluate_risque_itineraire(adresse_depart,
                                                         adresse_arrivee))

        if utilisation == "Savoir quel moyen de transport utiliser pour éviter les risques et avoir l'itinéraire correspondant.":
            print("Quelle est votre adresse de départ ?")
            adresse_depart = input("Entrez le nom de la rue, doit finir par ', New York' :")

            time.sleep(1)
            print("Quelle est votre adresse d'arrivée ?")
            adresse_arrivee = input("Entrez le nom de la rue, doit finir par ', New York' :")

            time.sleep(1)
            print(Particulier.eviter_zone_risquee(adresse_depart,
                                                  adresse_arrivee))


except KeyboardInterrupt:
    # faire CTRL C pour fermer l'application
    print()
    print("Fermeture de l'application")
    time.sleep(1)
    print("Nous espérons bientôt vous revoir !!!")
