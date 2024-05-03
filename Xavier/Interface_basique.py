#%% importation des modules
# from Utilisateur import Utilisateur
# from secteur_prive import SecteurPrive
# from secteur_public import SecteurPublic
# from particulier import Particulier
import tkinter as tk
import time
from particulier import Particulier
from secteur_prive import SecteurPrive

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

        if utilisation == "Déterminer le prix de mon assurance.":
            print("Quel véhicule souhaitez vous assurer ?")
            time.sleep(1)

            vehicule = choisi([])

            print("Entrez une liste de localisations que vous fréquentez "
                  "régulièrement.")

            localisation = choisi([])

            print("Le prix de votre assurance sera de :",
                  self.__donner_prix(data, localisation, vehicule))

    elif choix == "Secteur Public":
        print("En tant qu'acteur public que souhaitez vous faire ?")
        time.sleep(1)

        utilisation = choisi(["Connaître le taux de mortalité d'une rue.",
                              "Localiser une infrastructure."])

        if utilisation == "Connaître le taux de mortalité d'une rue.":
            print("Sur quelle rue souhaitez vous connaître le taux de mortalité ?")
            time.sleep(1)

            rue = choisi(Utilisateur.liste_modalites_variable(data, rue))

    elif choix == "Particulier":
        print("En tant que particulier que souhaitez vous faire ?")
        time.sleep(1)

        utilisation = choisi(["Déterminer un itinéraire.",
                              "Connaître le risque d'un itinéraire.",
                              "Savoir quel moyen de transport utiliser pour"
                              " éviter les risques."])

        if utilisation == "Déterminer un itinéraire.":
            print("Quelle est votre adresse de départ ?")
            adresse_arrivee = choisi(Particulier.liste_modalites_variables(data, rue))

            time.sleep(1)
            print("Quelle est votre adresse d'arrivée ?")
            adresse_depart = choisi(Particulier.liste_modalites_variable(data, rue))

            time.sleep(1)
            print("Voici l'itinéraire permettant de relier vos 2 adresses :",
                  Particulier.itineraires(adresse_arrivee, adresse_depart))

        if utilisation == "Connaître le risque d'un itinéraire.":
            print("Quelle est votre adresse de départ ?")
            adresse_arrivee = input(nom_rue ', New-York')

            time.sleep(1)
            print("Quelle est votre adresse d'arrivée ?")
            adresse_depart = choisi(Particulier.liste_modalites_variable(data, rue))

            time.sleep(1)
            print("Voici le risque de l'itinéraire permettant de relier vos 2 adresses :",
                  Particulier.evaluate_risque_itineraire(adresse_arrivee, adresse_depart))

        if utilisation == "Savoir quel moyen de transport utiliser pour éviter les risques.":
            print("Quelle est votre adresse de départ ?")
            adresse_arrivee = choisi(Particulier.liste_modalites_variables(data, rue))

            time.sleep(1)
            print("Quelle est votre adresse d'arrivée ?")
            adresse_depart = choisi(Particulier.liste_modalites_variable(data, rue))

            time.sleep(1)
            print("Voici l'itinéraire permettant de relier vos 2 adresses :",
                  Particulier.eviter_zone_risquee(adresse_arrivee, adresse_depart))


except KeyboardInterrupt:
    # faire CTRL C pour fermer l'application
    print()
    print("Fermeture de l'application")
    time.sleep(1)
    print("Nous espérons bientôt vous revoir !!!")
