import pandas as pd
import re


class Utilisateur:
    def nombre_observation(data):
        """
        Compte le nombre d'observations d'une base de données.

        Parameters
        ----------
        data : DataFrame
            La base de données dont on souhaite connaître le nombre
            d'observations.

        Returns
        -------
        list[str, int] :
            str : Phrase réponse.
            int : Nombre d'observations de la base de données.

        Raises
        ------
        TypeError: Si data n'est pas un DataFrame.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        return ["Nombre d'observations dans la base de données :",
                data.shape[0]]

    def calcul_totaux_statut(data, statut):
        """
        Calcule le nombre de blessés et/ou de tués.

        data : DataFrame
            Base de données sur laquelle on veut déterminer le nombre de
            blessés et/ou tués.

        statut : str
            Statut des victimes.
            B : blessées
            T : tuées
            BT : blessées et tuées

        Returns
        -------
        list[str, int] :
            str : Phrase réponse.
            int : Nombre de personnes blessées et/ou tuées selon le statut
              souhaité.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(statut, str):
            raise TypeError("Le statut doit être de type str.")

        if statut != "B" and statut != "T" and statut != "BT":
            raise ValueError("Le statut doit être B, T ou BT.")

        elif statut == "B":
            total_persons_injuried = data["NUMBER.OF.PERSONS.INJURED"].sum()
            return ["Nombre total de personnes blessées dans le tableau :",
                    total_persons_injuried]
        elif statut == "T":
            total_persons_killed = data["NUMBER.OF.PERSONS.KILLED"].sum()
            return ["Nombre total de personnes tuées dans le tableau :",
                    total_persons_killed]
        elif statut == "BT":
            total_persons_killed = data["NUMBER.OF.PERSONS.KILLED"].sum()
            total_persons_injuried = data["NUMBER.OF.PERSONS.INJURED"].sum()
            total_both = total_persons_killed + total_persons_injuried
            return ["Nombre total d'individus blessés et"
                    " tués dans le tableau :",
                    total_both]

    def calcul_totaux_cat_statut(data, categorie, statut):
        """
        Calcule le nombre de blessées et/ou de tués selon le type de personnes
        souhaité.

        data : DataFrame
            Base de données sur laquelle on veut déterminer le nombre de
            blessés et/ou tués.

        categorie : str
            Catégorie des personnes dont on veut déterminer le nombre
            de blessés et/ou tués.
            car : automobilistes
            cycle : cyclistes
            foot : piétons

        statut : str
            Statut des victimes.
            B : blessées
            T : tuées
            BT : blessées et tuées

        Returns
        -------
        list[str, int] :
            str : Phrase réponse.
            int : Nombre de personnes blessées et/ou tuées selon la catégorie
            souhaitée et le statut souhaité.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(statut, str):
            raise TypeError("Le statut doit être de type str.")

        if statut != "B" and statut != "T" and statut != "BT":
            raise ValueError("Le statut doit être B, T ou BT.")

        if not isinstance(categorie, str):
            raise TypeError("La catégorie doit être de type str.")

        if categorie != "cycle" and categorie != "car" and categorie != "foot":
            raise ValueError("La catégorie doit être car, cycle ou foot.")

        elif categorie == "car":
            colonnes_automobilistes = ["NUMBER.OF.MOTORIST.INJURED",
                                       "NUMBER.OF.MOTORIST.KILLED"]
            if statut == "B":
                total_automobilistes = data[colonnes_automobilistes[0]].sum()
                return ["Nombre total d'automobilistes blessés :",
                        total_automobilistes]
            elif statut == "T":
                total_automobilistes = data[colonnes_automobilistes[1]].sum()
                return ["Nombre total d'automobilistes tués :",
                        total_automobilistes]
            elif statut == "BT":
                total_automobilistes = data[colonnes_automobilistes].sum()\
                    .sum()
                return ["Nombre total d'automobilistes blessés et tués :",
                        total_automobilistes]

        elif categorie == "cycle":
            colonnes_cyclistes = ["NUMBER.OF.CYCLIST.INJURED",
                                  "NUMBER.OF.CYCLIST.KILLED"]
            if statut == "B":
                total_cyclistes = data[colonnes_cyclistes[0]].sum()
                return ["Nombre total de cyclistes blessés :",
                        total_cyclistes]
            elif statut == "T":
                total_cyclistes = data[colonnes_cyclistes[1]].sum()
                return ["Nombre total de cyclistes tués :",
                        total_cyclistes]
            elif statut == "BT":
                total_cyclistes = data[colonnes_cyclistes].sum().sum()
                return ["Nombre total de cyclistes blessés et tués :",
                        total_cyclistes]

        elif categorie == "foot":
            colonnes_piétons = ["NUMBER.OF.PEDESTRIANS.INJURED",
                                "NUMBER.OF.PEDESTRIANS.KILLED"]
            if statut == "B":
                total_piétons = data[colonnes_piétons[0]].sum()
                return ["Nombre total de piétons blessés :",
                        total_piétons]
            elif statut == "T":
                total_piétons = data[colonnes_piétons[1]].sum()
                return ["Nombre total de piétons tués :",
                        total_piétons]
            elif statut == "BT":
                total_piétons = data[colonnes_piétons].sum().sum()
                return ["Nombre total de piétons blessés et tués :",
                        total_piétons]

    # fonction de filtres
    def filtrer_par_nom_de_rue(data, street):
        """
        Filtre la base de données en fonction de la rue souhaitée.

        Parameters
        ----------
        data : DataFrame
            La base de données à filtrer.

        street : str
            Le nom de la rue selon laquelle nous souhaitons filtrer la base de
            données.

        Returns
        -------
        list[str, DataFrame] :
            str : Phrase réponse.
            DataFrame : La base de données filtrée contenant uniquement les
                        lignes où le nom de la rue correspond à street.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(street, str):
            raise TypeError("Le nom de la rue doit être de type str.")

        for char in street:
            if not (char.isupper() or char.isspace()):
                raise ValueError("Le nom de la rue doit contenir uniquement"
                                 " des majuscules et des espaces")

        filtered_data = data[data["CROSS.STREET.NAME"].str.contains(street) |
                             data["ON.STREET.NAME"].str.contains(street) |
                             data["OFF.STREET.NAME"].str.contains(street)]
        return ["Base de données filtrée pour la rue nomée:",
                street, filtered_data]

    def filtrer_par_date(data, date_debut, date_fin):
        """
        Filtre le DataFrame en fonction de la date entre date_debut
        et date_fin inclus.

        Parameters
        ----------
        data : DataFrame
            La base de données à filtrer.

        date_debut : str
            La date de début de la période choisie au format "MM/DD/YYYY".

        date_fin : str
            La date de fin de la période choisie au format "MM/DD/YYYY".

        Returns
        -------
        list : Une liste contenant un message décrivant la période filtrée
            et le DataFrame filtré entre le jour de début et de fin de
            la période.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(date_debut, str):
            raise TypeError("La date début doit être un str.")

        if not re.match(r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/[0-9]{4}$',
                        date_debut):
            raise ValueError("La date début doit être au format 'MM/JJ/AAAA'.")

        if not isinstance(date_fin, str):
            raise TypeError("La date fin doit être un str.")

        if not re.match(r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/[0-9]{4}$',
                        date_fin):
            raise ValueError("La date fin doit être au format 'MM/JJ/AAAA'.")

        if date_debut > date_fin:
            raise ValueError("La date de début ne doit pas être supérieure"
                             " à la date de fin.")

        # Convertir les colonnes "CRASH.DATE" en type datetime
        data["CRASH_DATE"] = pd.to_datetime(data["CRASH.DATE"])

        # Les bornes sont prises
        filtered_data = data[(data["CRASH_DATE"] >= pd.to_datetime(date_debut))
                             &
                             (data["CRASH_DATE"] <= pd.to_datetime(date_fin))]

        # Supprimer la colonne temporaire "CRASH_DATE"
        filtered_data = filtered_data.drop(columns=["CRASH_DATE"])

        return ["Base de données filtrée pour la période du",
                date_debut,
                "au",
                date_fin,
                filtered_data]

    def filtrer_par_heure(data, heure_debut, heure_fin):
        """
        Filtre le DataFrame en fonction de l'heure entre heure_debut
        et heure_fin inclus.

        Parameters
        ----------
        data : DataFrame
            La base de données à filtrer.

        heure_debut : str
            L'heure de début de la période au format "HH:MM".

        heure_fin : str
            L'heure de fin de la période au format "HH:MM".

        Returns
        -------
        list : Une liste contenant un message décrivant la période filtrée
            et le DataFrame filtré.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(heure_debut, str):
            raise TypeError("L'heure de début doit être un str")

        # Ne prends pas 24h00 mais prend 00:00

        if not re.match(r'^(2[0-3]|[01][0-9]):[0-5][0-9]$', heure_debut):
            raise ValueError("L'heure de début doit être au format 'HH:MM'.")

        if not isinstance(heure_fin, str):
            raise TypeError("L'heure de fin doit être un str")

        if not re.match(r'^(2[0-3]|[01][0-9]):[0-5][0-9]$', heure_fin):
            raise ValueError("L'heure de fin doit être au format 'HH:MM'.")

        if heure_debut > heure_fin:
            raise ValueError("L'heure de début ne doit pas être supérieure"
                             " à l'heure de fin.")

        # Convertir les colonnes "CRASH.TIME" en type datetime
        data["CRASH_TIME"] = pd.to_datetime(data["CRASH.TIME"]).dt.\
            strftime("%H:%M")

        # Filtrer le DataFrame en fonction de l'heure entre heure_debut
        # et heure_fin inclusivement
        filtered_data = data[(data["CRASH_TIME"] >= heure_debut) &
                             (data["CRASH_TIME"] <= heure_fin)]

        # Supprimer la colonne temporaire "CRASH_TIME"
        filtered_data = filtered_data.drop(columns=["CRASH_TIME"])

        return ["Base de données filtrée pour la période entre",
                heure_debut,
                "et",
                heure_fin, ":",
                filtered_data]

    def filtrer_par_modalite_variable(data, variable, modalite):
        """
        Filtre la base de données en fonction d'une modalité spécifique d'une
        variable spécifique et renvoie la base de données filtrée.

        Parameters
        ----------
        data : DataFrame
            La base de données à filtrer.

        variable : str
            La variable spécifique à filtrer.

        modalite : str
            La modalité spécifique à filtrer.

        Returns
        -------
        list : Une liste contenant un message décrivant la modalité filtrée
        d'une certaines variable et le DataFrame filtré.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if variable not in Utilisateur.liste_variables_dataframe(data)[-1]:
            raise ValueError("Cette variable n'est pas dans la base de "
                             "données.")

        L_mod_var = Utilisateur.liste_modalites_variable(data, variable)[-1]
        if modalite not in L_mod_var:
            raise ValueError("Cette modalité n'existe pas pour la variable "
                             "choisie.")

        filtered_data = data[data[variable] == modalite]
        return ["Base de données filtrée pour la modalité",
                modalite,
                "de la variable",
                variable,
                filtered_data]

    # fonction listant les modalités et les variables d'un dataframe

    def liste_variables_dataframe(data):
        """
        Renvoie la liste des variables (colonnes) d'une base de données.

        Parameters
        ----------
        data : DataFrame
            La base de données dont on souhaite la liste des variables.

        Returns
        -------
        list : Liste des variables (colonnes) de la base de données.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        liste_variable = data.columns.tolist()
        return ["Liste des variables de la base de données :",
                liste_variable]

    def liste_modalites_variable(data, variable):
        """
        Renvoie toutes les modalités différentes d'une variable d'une base de
        données.

        attention varible en majuscule et séparer les mots par des points

        Parameters
        ----------
        data : DataFrame
            La base de données dont on souhaite obtenir les modalités d'une de
            ses variables.

        variable : str
            Variable dont on souhaite obtenir toutes les modalités.

        Returns
        -------
        list : Liste des modalités différentes de la variable.

        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("La base de données doit être un DataFrame.")

        if not isinstance(variable, str):
            raise TypeError("La variable doit être de type str.")

        if not re.match(r'^[A-Z0-9.]+$', variable):
            raise ValueError("La variable ne doit contenir que "
                             "des majuscules, des points, des nombres "
                             "et pas d'espace.")

        List_Variables = Utilisateur.liste_variables_dataframe(data)
        if variable not in List_Variables[-1]:
            raise ValueError("Cette variable n'est pas dans la base de "
                             "données.")

        liste_modalites = list(data[variable].unique())
        return ["Liste des modalités différentes de la variable :",
                variable, liste_modalites]

    # fonction avancée
    def danger_rue(data, street, categorie):
        """
        Permet de calculer le danger d'une rue en %.

        Parameters
        ----------
        data : Dataframe
            base de données sur laquelle nous travaillons.

        street : str
            Nom de la rue pour laquelle nous souhaitons déterminer le danger.

        categorie : str
            Catégorie d'usagés : piéton, cycliste ou automobiliste.

        Returns
        -------
        str : Phrase indiquant le danger en % pour la rue et la catégorie
              souhaitées.

        """
        data_street = Utilisateur.filtrer_par_nom_de_rue(data, street)[-1]
        n_tot = Utilisateur.nombre_observation(data)[-1]
        if n_tot == 0:
            return ["Il n'y a pas d'accident ou bien le tableau est vide.",
                    "Pour la rue :", street,
                    "Il y a un rique (en %) de :", 0]
        else:
            n_T = Utilisateur.\
                calcul_totaux_cat_statut(data_street, categorie, "T")[-1]
            n_B = Utilisateur.\
                calcul_totaux_cat_statut(data_street, categorie, "B")[-1]
            risque = (n_T + (1/4)*n_B) / (n_T + n_B)
            return ["Pour la rue :", street,
                    "il y a un rique (en %) de :", risque]



# # Fonction pour classer si c'est jour ou nuit
# def classer_jour_nuit(self, heure):
#     if heure.hour >= 6 and heure.hour < 18:
#         return 'jour'
#     else:
#         return 'nuit'

# # Appliquer la fonction pour créer une nouvelle colonne 'Jour_Nuit'
# df['Jour_Nuit'] = df['CRASH.TIME'].apply(classer_jour_nuit)

# def risque_nuit_jour(self, data,utilisateur) :
#     jour=2
#     nuit=2
#     if data['Jour_Nuit']=='jour':
#         if jour==0 :
#                 return 0
#         else :
#              return jour/(jour+nuit)
#     else :
#         if nuit==0 :
#                 return 0
#         else :
#                 return nuit/(jour+nuit)

# def risque_voiture(self, data, utilisateur, voiture):
#     if voiture in data['VEHICLE.TYPE.CODE.1'].values:
#         # Regroupement par 'VEHICLE.TYPE.CODE.1' et comptage des occurrences de 'COLLISION_ID'
#         regroupement = df.groupby('VEHICLE.TYPE.CODE.1')['COLLISION_ID'].count()
#         return regroupement[voiture]/max(regroupement.iloc[:, 1])
#     else:
#         return 0

# def risque_rue(self, data, rue):
#      if rue in data["CROSS.STREET.NAME"].values or in data["OFF.STREET.NAME"].values or in data["ON.STREET.NAME"].values:
#         # calcul des nombres de bléssés/morts
#         regroupement = filtre(data, rue)[-1]
#         nombre_BT_rue= calcul_totaux_statut(regroupement, BT)[1]
#         nombre_BT= max(calcul_totaux_statut(data, BT)[1])
#         return nombre_BT_rue/nombre_BT
#      else:
#         return 0
